bind = "0.0.0.0:8000"
backlog = 2048
workers = 3
chdir = "/learn"
pidfile = None
accesslog = "/home/uwsgi/log/gunicorn/gunicorn_access.log"
errorlog = "/home/uwsgi/log/gunicorn/gunicorn_error.log"
debug = False
loglevel = "info"
user = "uwsgi"
group = "uwsgi"