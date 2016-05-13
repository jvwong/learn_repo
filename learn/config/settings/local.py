from .base import *

DEBUG = True

# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1']

DATABASE = ".".join([PROJECT_NAME, "db"])
# DATABASE_NAME = os.path.abspath(os.path.join(REPO_DIR, "database", DATABASE))
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2'
#         'NAME': DATABASE_NAME,
#         # The following settings are not used with sqlite3:
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#         'PORT': '',                      # Set to empty string for default.
#     }
# }

INSTALLED_APPS += []