#!/usr/bin/env bash

# Creates a tar.gz dump of the Docker postgres data container
# Note: the volume sits on the virtualbox in OSX.

## DATA_VOLUME_MOUNT
## docker volume ls
## docker volume inspect <volume name>
DB_CONTAINER="learn_db"
WEB_CONTAINER="learn_web"
UNAME="uwsgi"

# Variables
YEAR_DIR=$(date +%Y)
MONTH_DIR=$(date +%m)
DAY_DIR=$(date +%d)

# Declare the local directory to dump to
DB_BACKUP_PATH="${HOME}/backups/db/${YEAR_DIR}/${MONTH_DIR}/${DAY_DIR}"
MEDIA_BACKUP_PATH="$HOME/backups/media/${YEAR_DIR}/${MONTH_DIR}/${DAY_DIR}"
​
#Backup Postgres Database to BACKUP_PATH
docker run --rm \
  --volumes-from ${DB_CONTAINER} \
  -v ${DB_BACKUP_PATH}:/backup busybox \
  tar -zcvf /backup/postgres-$(date +%Y-%m-%d-%H%M).tar.gz /var/lib/postgresql/data

  #Backup MEDIA_ROOT @/home/uwsgi/media to BACKUP_PATH
  docker run --rm \
    --volumes-from ${WEB_CONTAINER} \
    -v ${MEDIA_BACKUP_PATH}:/backup busybox \
    tar -zcvf /backup/media-$(date +%Y-%m-%d-%H%M).tar.gz /home/$UNAME/media
