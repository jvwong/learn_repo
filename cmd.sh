#!/bin/bash
# Runs under USER specified by Dockerfile

# exits if any non-zero return
set -e

if [ "$ENV" = 'DEV' ]; then
	echo "Running Development Server"
    exec gunicorn -c /learn/config/gunicorn_dev.py config.wsgi:application
else
	echo "No Production Server configured"
fi
