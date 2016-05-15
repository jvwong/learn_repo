# Learn Project

## Docker 

### Use Compose to build the image
```
 $ docker-compose run web python manage.py migrate
```
This instructs Compose to run ```python manage.py migrate``` in a container, using the web service’s image and configuration. Because the web image doesn’t exist yet, Compose builds it from the current directory, as specified by the build: . line in docker-compose.yml.

Once the web service image is built, Compose runs it and executes the ```python manage.py migrate``` command in the container. This command instructs Django to create the database models.


```
 $ docker-compose up -d
```

This runs the app (background).


## Create Super User
Now create a super user inside the running container:
```
 $ docker exec -it learnrepo_web_1 /bin/bash    
 root@:/learn# python manage.py createsuperuser
 ...
 root@:/learn# exit
```

## Database migrations
When the model is changed, this must be versioned and commited. Within a running container:
```
 $ docker exec learnrepo_web_1 python manage.py makemigrations
 $ docker exec learnrepo_web_1 python manage.py migrate 
```

## Backup the postgresql data volume 
See the official Docker [docs](https://docs.docker.com/engine/userguide/containers/dockervolumes/)
```
 $ docker run --rm --volumes-from <data volume container name> -v /Users/jeffreywong/backups:/backup debian tar cvf /backup/backup.tar /var/lib/postgresql/data
```
Note: the official postgres Dockerfile defines a volume at /var/lib/postgresql/data.

* Here you’ve launched a new container and mounted the volume from the 'data volume container name'.
* You’ve then mounted a local host directory ($pwd) as /backup inside the new (anonymous) container. 
* Finally, you’ve passed a command that uses tar to backup the contents of the ```/var/lib/postgresql/data``` (source) volume to a backup.tar file inside our /backup (target) directory. When the command completes and the container stops we’ll be left with a backup of our ```/var/lib/postgresql/data``` volume. 

Let's say that you wish to restore to the learn_data container 
Un-tar the backup file in that container's data volume.
```
    docker cp [OPTIONS] SRC_PATH | - CONTAINER:DEST_PATH
```
```
 $  docker run --rm --volumes-from learn_data -v ~/backups/:/backup debian tar xvf /backup/backup.tar 
```
