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
 $ docker run --rm --volumes-from <dbdata container name> -v $(pwd):/backup debian tar cvf /backup/backup.tar /var/lib/postgresql/data
```
Here you’ve launched a new container and mounted the volume from the dbstore container. You’ve then mounted a local host directory as /backup. Finally, you’ve passed a command that uses tar to backup the contents of the dbdata volume to a backup.tar file inside our /backup directory. When the command completes and the container stops we’ll be left with a backup of our dbdata volume.

Then un-tar the backup file in a container`s data volume.
```
 $ docker run --rm --volumes-from <dbdata container name> -v $(pwd):/backup ubuntu bash -c "cd /dbdata && tar xvf /backup/backup.tar --strip 1"
```
