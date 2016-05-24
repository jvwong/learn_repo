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

RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g less

EXPOSE 8000

# Runing Django as uwsgi - requires writeable directories
USER uwsgi
RUN mkdir -p ~/static ~/media
RUN mkdir -p ~/log/gunicorn
RUN touch ~/log/gunicorn/gunicorn_access.log
RUN touch ~/log/gunicorn/gunicorn_error.log

COPY cmd.sh /
CMD ["/cmd.sh"]


