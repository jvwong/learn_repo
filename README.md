# Learn Project

## Docker 

### Install some helpful setup commands (OSX)
Command-completion
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
 eval $(docker-machine env default)
```


### Create new dockeradmin user on remote server with private-public key authentication.
Create a new user on the remote host and allow sudo access: 
```
 remote$ sudo adduser dockeradmin
```

Add the following to /etc/sudoers
```
 remote$ sudo visudo
 
 ...
 dockeradmin ALL=(ALL) NOPASSWD: ALL
```

If you've locked down your server, you may need to update the ssh user access:
```
 remote$ sudo vim /etc/ssh/sshd_config
 ... 
  
 AllowUsers ... dockeradmin ...
```

Perform all remote ssh login with keys. Generate the public (id_rsa.pub) and private (id_rsa) keys in ~/.ssh:
```
 local$ ssh-keygen
```

Create an authorized_keys in the .ssh directory of the remote computer that you want to connect to: 
```
 remote$ su - dockeradmin
 dockeradmin@remote$ mkdir .ssh
 dockeradmin@remote$ chmod 700 .ssh
```

Paste in your local public key into `~/.ssh/authorized_keys`.

Restrict the permissions:
```
 dockeradmin@remote-server:~$ chmod 600 .ssh/authorized_keys
```

Reboot the server just in case.

### Create a generic host [docs](https://docs.docker.com/machine/drivers/generic/)
These are the relevant fields for the docker-machine create command:
```
 docker-machine create -d generic 
   --generic-ip-address {ip-address} \
   --generic-ssh-key {private-key} \
   --generic-ssh-user {username} \
   --generic-ssh-port {ssh-port} {docker-vm-name}
```
 So this would translate to something like this for a docker-vm-name of `docker-serve`:
 
```
 local$ docker-machine create --driver generic --generic-ip-address=192.168.0.10 --generic-ssh-key=$HOME/.ssh/id_rsa --generic-ssh-user=dockeradmin --generic-ssh-port=22 docker-serve
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
 local$ docker-machine ls 
 local$ eval $(docker-machine env docker-serve)
 local$ docker run hello-world
```


*Note 1: You may see a ``Error: Failed to get d-bus connection: operation not permitted` in Ubuntu 15.04. Upgrade to 15.10*  

*Note 2: Error: `Client is newer than server (client API version: 1.22, server API version: 1.21)`; Update the apt sources [accordingly](https://blog.docker.com/2015/07/new-apt-and-yum-repos/)*
```
    # add the new gpg key
    remote$ sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
    
    # edit your /etc/apt/sources.list.d/docker.list
    remote$ sudo vim /etc/apt/sources.list.d/docker.list
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


### Create a Digital Ocean [host](https://docs.docker.com/machine/examples/ocean/)
Create an API token from your Digital Ocean account. Be sure to give it write access.

Store this token (LEARN_DO_TOKEN) as an env variable for convenience:
```
 local$ vim ~/.bash_profile
 ... 
 LEARN_DO_TOKEN=<your token here>
 ...
 local$ source ~/.bash_profile
 local$ echo $LEARN_DO_TOKEN # Should output the token 
```

Create the remote hostnamed `learn-do`:
```
 local$ docker-machine create --driver digitalocean --digitalocean-access-token $LEARN_DO_TOKEN learn-do
```

Check the creation:
```
 local$ docker-machine ls
```

Activate it:
```
 local$ eval $(docker-machine env learn-do)
```

Run the alternative remote script (docker-compose-remote-ssd.yml):
```
 $ docker-compose --file=docker-compose-remote-ssd.yml run web python manage.py makemigrations cases
 $ docker-compose --file=docker-compose-remote-ssd.yml run web python manage.py migrate
 $ docker-compose --file=docker-compose-remote-ssd.yml up -d
```

### Development: Use Compose to run the containers locally
```
 $ docker-compose run web 
```
This instructs Compose to run ```python manage.py migrate``` in a container, using the web service’s image and configuration. Because the web image doesn’t exist yet, Compose builds it from the current directory, as specified by the build: . line in docker-compose.yml.

Once the web service image is built, Compose runs it and executes the ```python manage.py migrate``` command in the container. This command instructs Django to create the database models.


```
 $ docker-compose up -d
```

This runs the app (background).

List the volumes: You should see `learnrepo_dbdata` named volume. 
```
 $ docker volume ls
 $ docker volume inspect learnrepo_dbdata
```
You should see something like this for the `inspect`:
```
 [
    {
        "Name": "learnrepo_dbdata",
        "Driver": "local",
        "Mountpoint": "/mnt/sda1/var/lib/docker/volumes/learnrepo_dbdata/_data"
    }
]
```

## Starting from scratch
### Create Super User
Now create a super user inside the running container:
```
 $ docker exec -it learnrepo_web_1 /bin/bash    
 root@:/learn# python manage.py createsuperuser
 ...
 root@:/learn# exit
```

### Database migrations
When the model is changed, this must be versioned and commited. Within a running container:
```
 $ docker exec learnrepo_web_1 python manage.py makemigrations
 $ docker exec learnrepo_web_1 python manage.py migrate 
```


## Data Backup & Restoration
### Backup 
The bash script `backup.sh` in the backups directory will dump the entire data volume into a tar file on the local machine. 
*Note: the official postgres Dockerfile defines a volume at /var/lib/postgresql/data.*
```
 asd
```
* Here we launch a new container (busybox), using the volumes of `DATA_CONTAINER_NAME` via the `--volumes-from` option
* Mount a user-defined host directory `BACKUP_PATH` as /backup inside the new container 
* Finally, tar the contents of `/var/lib/postgresql/data` in `DATA_CONTAINER_NAME` 

### Restore
Rebuild the services. Stop the containers as docker-compose auto-launches db service.
```
 $ docker-compose run web python manage.py makemigrations cases 
 $ docker-compose run web python manage.py migrate 
 $ docker-compose stop 
```

Dump the data into the database container (learnrepo_db):
```
 $ docker run --volumes-from learn_db -v /Users/jeffreywong/backups/2016/05/16:/backup busybox tar xvfz /backup/postgres-2016-05-16-0935.tar.gz
```

Run the web app
```
 $ docker-compose up 
```

## Image distribution
### [Docker Hub](https://hub.docker.com/)
You'll need to sign up for an account at Docker Hub first. 
Login via cli:
```
 local$ docker login
```

Build the image (learnweb) with tag (0.1) and push to the Docker Hub:
```
 local$ cd <repo directory>
 local$ docker build -t "learnweb:0.1" .
 local$ docker tag "learnweb:0.1" "jvwong/learnweb:0.1"
 local$ docker push jvwong/learnweb:0.1
```
