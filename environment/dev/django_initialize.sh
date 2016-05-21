#!/usr/bin/env bash
set -e

# Collect static files
# This is tricky - IMAGE directories declared as VOLUME will be hidden by HOST
# i.e. HOST -| IMAGE but you can manipulate the CONTAINER as below
# Must be run as root as container user is uwsgi as set in Dockerfile
echo "Collect static"
docker-compose run --rm --user="root" web python manage.py collectstatic --no-input

echo "Run migrations"
docker-compose run --rm web python manage.py makemigrations --no-input
docker-compose run --rm web python manage.py migrate --no-input

