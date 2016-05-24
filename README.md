# Learn Project

## Django
### Create Super User
Now create a super user inside the running container:
```
$ docker exec -it learnrepo_web_1 /bin/bash    
root@:/learn# python manage.py createsuperuser
...
root@:/learn# exit
```

### Database migrations
This is contained in the `django_initialize.sh` utility.

### Testing
Assuming that the web container is running, just hook in:
```
$ docker exec -it learn_web python manage.py test <optional: dot-separated module>
```

### Bower packages
To avoid the volumes permission issues, Dockerfile installs bower packages in /tmp then copies this to STATIC_ROOT (/home/uwsgi/static)


## Docker
### Install some helpful setup commands (OSX)
To make life easier, install the command-completion scripts

```
files=(docker-machine docker-machine-wrapper docker-machine-prompt)
for f in "${files[@]}"; do
  curl -L https://raw.githubusercontent.com/docker/machine/v$(docker-machine --version | tr -ds ',' ' ' | awk 'NR==1{print $(3)}')/contrib/completion/bash/$f.bash > `brew --prefix`/etc/bash_completion.d/$f
done
```

Start default on Boot in OSX. Create `~/Library/LaunchAgents/com.docker.machine.default.plist`

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>EnvironmentVariables</key>
        <dict>
            <key>PATH</key>
            <string>/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin</string>
        </dict>
        <key>Label</key>
        <string>com.docker.machine.default</string>
        <key>ProgramArguments</key>
        <array>
            <string>/usr/local/bin/docker-machine</string>
            <string>start</string>
            <string>default</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
    </dict>
</plist>
```
Then add the following to your ~.bash_profile
```
$ eval $(docker-machine env default)
```


### Create new docker user on remote
Create a new user on the remote host and allow sudo access:
```
$ sudo adduser dockeradmin
```

Add the following to /etc/sudoers
```
$ sudo visudo
...
dockeradmin ALL=(ALL) NOPASSWD: ALL
```

If you've locked down your server, you may need to update the ssh user access:
```
$ sudo vim /etc/ssh/sshd_config
...
AllowUsers ... dockeradmin ...
```

Perform all remote ssh login with keys. Generate the public (id_rsa.pub) and private (id_rsa) keys in ~/.ssh:
```
$ ssh-keygen
```

Create an authorized_keys in the .ssh directory of the remote computer that you want to connect to:
```
$ su - dockeradmin
$ mkdir .ssh
$ chmod 700 .ssh
```

Paste in your local public key into `~/.ssh/authorized_keys`.

Restrict the permissions:
```
$ chmod 600 .ssh/authorized_keys
```

Reboot the server just in case. You can also disable password authentication on the remote server now:
```
$ sudo vim /etc/ssh/sshd_config
...
ChallengeResponseAuthentication no
PasswordAuthentication no
UsePAM no
```

### Create a generic host [docs](https://docs.docker.com/machine/drivers/generic/)
These are the relevant fields for the docker-machine create command:
```
$ docker-machine create -d generic
 --generic-ip-address {ip-address} \
 --generic-ssh-key {private-key} \
 --generic-ssh-user {username} \
 --generic-ssh-port {ssh-port} {docker-vm-name}
```
 So this would translate to something like this for a docker-vm-name of `docker-serve`:

```
$ docker-machine create --driver generic --generic-ip-address=192.168.0.10 --generic-ssh-key=$HOME/.ssh/id_rsa --generic-ssh-user=dockeradmin --generic-ssh-port=22 docker-serve
```

You should see some commands related to provisioning the remote server, copying certs...
```
Importing SSH key...
Waiting for machine to be running, this may take a few minutes...
Detecting operating system of created instance...
Waiting for SSH to be available...
Detecting the provisioner...
Provisioning with ubuntu(systemd)...
Installing Docker...
Copying certs to the local machine directory...
Copying certs to the remote machine...
Setting Docker configuration on the remote daemon...
Checking connection to Docker...
Docker is up and running!
```

Make sure it works:
```
$ docker-machine ls
$ eval $(docker-machine env docker-serve)
$ docker run hello-world
```

>Note 1: You may see a 'Error: Failed to get d-bus connection: operation not permitted' in Ubuntu 15.04. Upgrade to 15.10  


>Note 2: Error: 'Client is newer than server (client API version: 1.22, server API version: 1.21)'; Update the apt sources [accordingly](https://blog.docker.com/2015/07/new-apt-and-yum-repos/)

```
# add the new gpg key
$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

# edit your /etc/apt/sources.list.d/docker.list
$ sudo vim /etc/apt/sources.list.d/docker.list
...
# Ubuntu Wily
deb https://apt.dockerproject.org/repo ubuntu-wily main
...

$ sudo apt-get update    
# remove the old
$ sudo apt-get purge lxc-docker*     
# install the new
$ sudo apt-get install docker-engine
```


## Named Volume Backup & Restoration
The two main items to be concerned with are Postgres data and assets in MEDIA_ROOT (e.g. pdf, images). Let's grab these every once and a while.

> Note: the official postgres Dockerfile defines a volume at /var/lib/postgresql/data.

### Backup
Backup the database and media content with `Docker/utilities/backup.sh`. This will dump the entire data volume into a tar file on the local machine inside s`~/backups/<yr>/<mth>/<d>/postgres-<yr>-<mth>-<d>-<hrmin>.tar.gz`. See [Restore](###Restore) on how to dump to target database.

### Restore
#### Local
Stop the containers then dump the data directly into the fresh database container (learnrepo_db):
```
$ docker-compose stop  
$ docker run --rm --volumes-from learn_db -v /Users/jeffreywong/backups/2016/05/22:/backup busybox tar xvfz /backup/postgres-2016-05-22-0954.tar.gz
```
Let's try that for media files too:
```
$ docker-compose stop  
$ docker run --rm --volumes-from learn_web -v /Users/jeffreywong/backups/media/2016/05/24:/backup busybox tar xvfz /backup/media-2016-05-24-1257.tar.gz
```


#### Remote Host
Of course, use docker-machine to hook into the remote machine (docker-serve).
```
$ docker-machine ls
$ eval $(docker-machine env docker-serve)
$ docker-machine active  # docker-serve
```

Let's make a remote backup directory then scp our tar archive into it.
```
$ docker-machine ssh docker-serve pwd  # /home/dockeradmin
$ docker-machine ssh docker-serve mkdir backups
$ docker-machine scp ~/backups/<path/to/tar.gz> docker-serve:~/backups
```

Get the volume associated with the database container (learn_db):
```
$ docker run --rm --volumes-from learn_db -v /home/dockeradmin/backups:/backup busybox tar xvfz /backup/<tar.gz file>
```

Do same for media.
