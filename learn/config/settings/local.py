from .base import *
import os
from .secret_key import SECRET_KEY_DEFAULT

SECRET_KEY = bool(os.environ.get('SECRET_KEY', SECRET_KEY_DEFAULT))

# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1']

DATABASE = ".".join([PROJECT_NAME, "db"])
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE,
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432'
    }
}

INSTALLED_APPS += []

