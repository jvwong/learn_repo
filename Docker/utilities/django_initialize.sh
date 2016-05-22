#!/usr/bin/env bash
set -e

# This file assumes you have a running web app with container named learn_web

# Collect static files
# This is tricky - IMAGE directories declared as VOLUME will be hidden by HOST
# i.e. HOST -| IMAGE but you can manipulate the CONTAINER as below
# Must be run as root as container user is uwsgi as set in Dockerfile
echo "Collect static"
docker exec -it --user="root" learn_web python manage.py collectstatic --no-input

echo "Run migrations"
docker exec -it --user="root" learn_web python manage.py makemigrations --no-input
docker exec -it --user="root" learn_web python manage.py migrate --no-input

