#!/bin/bash
# Runs under USER specified by Dockerfile

# exits if any non-zero return
set -e

if [ "$ENV" = 'DEV' ]; then
	echo "Running Development Server"
    exec gunicorn -c /learn/config/gunicorn_dev.py config.wsgi:application
elif [ "$ENV" = 'UNIT' ]; then
    echo "Running unit tests"
    # This needs a bunch of environment variables for Django set.
    #exec python manage.py test
else
	echo "No Production Server configured"
fi
