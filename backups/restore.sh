#!/usr/bin/env bash

# Re-create the services
# docker-compose up -d

# Create a dummy container, mount the data container volume, then dump the tar into their 'shared' directory
# docker run --volumes-from learn_data -v /Users/jeffreywong/backups/2016/05/16:/backup busybox tar xvfz /backup/postgres-2016-05-16-0935.tar.gz

# Run the database container/web
# docker-compose run -d db
