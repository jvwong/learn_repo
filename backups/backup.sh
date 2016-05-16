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