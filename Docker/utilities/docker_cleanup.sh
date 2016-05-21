#!/usr/bin/env bash
#
#### Stop containers, delete them, then get rid of dangling images.
# docker stop $(docker ps -aq)
# docker rm -v $(docker ps -aq)

#### Remove dangling images
docker rmi $(docker images -f "dangling=true" -q)

#### Get rid of dangling volumes
#### use docker 'rm -v' when deleting containers OR
#### add the --rm flag with 'docker run'
docker volume rm $(docker volume ls -fq dangling=true)

## remove stopped containers
docker rm -v $(docker ps -aq -f="exited=0")
docker rm -v $(docker ps -aq -f="exited=1")