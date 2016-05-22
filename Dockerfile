FROM python:3.5.1

# create the user
RUN groupadd -r uwsgi && useradd -r -m -g uwsgi uwsgi

# Install dependencies
ADD requirements.txt /tmp/requirements.txt
RUN cd /tmp && pip install -r requirements.txt

# Create the project directory
RUN mkdir /learn
WORKDIR /learn
COPY learn /learn

EXPOSE 8000
USER uwsgi

# Temp -- see logging chapter
RUN mkdir -p ~/log/gunicorn
RUN touch ~/log/gunicorn/gunicorn_access.log
RUN touch ~/log/gunicorn/gunicorn_error.log

COPY cmd.sh /
CMD ["/cmd.sh"]


