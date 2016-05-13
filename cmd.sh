#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
    echo "Run Gunicorn"
    echo "if not django.contrib.auth.models.User.objects.filter(username='admin').count(): django.contrib.auth.models.User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
	exec gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload --log-file=-
else
	echo "Running Production Server"
fi
