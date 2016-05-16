# Learn Project

## Docker 

### Use Compose to build the image
```
 $ docker-compose run web 
```
This instructs Compose to run ```python manage.py migrate``` in a container, using the web service’s image and configuration. Because the web image doesn’t exist yet, Compose builds it from the current directory, as specified by the build: . line in docker-compose.yml.

Once the web service image is built, Compose runs it and executes the ```python manage.py migrate``` command in the container. This command instructs Django to create the database models.


```
 $ docker-compose up -d
```

This runs the app (background).

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


## Performing Backups
### Backup the postgresql data volume
The bash script `backup.sh` in the backups directory will dump the entire data volume into a tar file on the local machine. 
*Note: the official postgres Dockerfile defines a volume at /var/lib/postgresql/data.*
```
 #!/usr/bin/env bash

 # Creates a tar.gz dump of the Docker postgres data container
 DATA_CONTAINER_NAME=learn_data

 # Variables
 YEAR_DIR=$(date +%Y)
 MONTH_DIR=$(date +%m)
 DAY_DIR=$(date +%d)

 # Declare the local directory to dump to
 BACKUP_PATH="/Users/jeffreywong/backups/${YEAR_DIR}/${MONTH_DIR}/${DAY_DIR}"

 mkdir -p ${BACKUP_PATH}
​
 #Backup Postgres Database to BACKUP_PATH
 docker run --rm \
   --volumes-from ${DATA_CONTAINER_NAME} \
   -v ${BACKUP_PATH}:/backup busybox \
   tar -zcvf /backup/postgres-$(date +%Y-%m-%d-%H%M).tar.gz /var/lib/postgresql/data
```
* Here we launch a new container (busybox), using the volumes of `DATA_CONTAINER_NAME` via the `--volumes-from` option
* Mount a user-defined host directory `BACKUP_PATH` as /backup inside the new container 
* Finally, tar the contents of `/var/lib/postgresql/data` in `DATA_CONTAINER_NAME` 

### Dump the postgresql database
## Into host directory 
```
 $ docker run --interactive \
 
```
 

## Starting from a previous backup of postgresql
Inside the copy the tarball to the learn_db container and unpack into `/var/lib/postgresql/data`: 
```
 $ docker cp ~/backups/backup.tar learn_db:/tmp
 $ docker exec -it learn_db tar xvf /tmp/backup.tar --strip=4 --directory /var/lib/postgresql/data 
```
Restart the containers.
```
 $ docker-compose restart
 
```

## Saving the learn_web local media files etc...?