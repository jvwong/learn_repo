#!/usr/bin/env bash

# Creates a tar.gz dump of the Docker postgres data container
# Note: the volume sits on the virtualbox in OSX.

## DATA_VOLUME_MOUNT
## docker volume ls
## docker volume inspect <volume name>
DB_CONTAINER="learn_db"

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
  --volumes-from ${DB_CONTAINER} \
  -v ${BACKUP_PATH}:/backup busybox \
  tar -zcvf /backup/postgres-$(date +%Y-%m-%d-%H%M).tar.gz /var/lib/postgresql/data