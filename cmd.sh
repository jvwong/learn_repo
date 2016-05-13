#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
	echo "Running Development Server"
	exec gunicorn config.wsgi:application -b 0.0.0.0:8000 --reload --log-file=-
	# exec python manage.py runserver 0.0.0.0:8000
else
	echo "Running Production Server"
fi
