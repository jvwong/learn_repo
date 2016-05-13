#!/bin/bash

# create database with running container
exec docker exec learnrepo_db_1 createdb -Upostgres learn.db
exec docker exec learnrepo_learn_1 python manage.py makemigrations
exec docker exec learnrepo_learn_1 python manage.py migrate
echo "[run] create superuser"
exec docker exec learnrepo_learn_1 echo "if not django.contrib.auth.models.User.objects.filter(username='admin').count(): django.contrib.auth.models.User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell

