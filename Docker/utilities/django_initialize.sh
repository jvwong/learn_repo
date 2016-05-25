#!/usr/bin/env bash
set -e

# This file assumes you have a running web app with container named learn_web

echo "Collect static"
docker exec -it --user="uwsgi" learn_web python manage.py collectstatic --no-input

#echo "Run migrations"
docker exec -it --user="root" learn_web python manage.py makemigrations cases thumbnail --no-input
docker exec -it --user="root" learn_web python manage.py migrate --no-input
