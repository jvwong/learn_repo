FROM python:3.5.1

# create the user
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi

# Install dependencies
ADD requirements/base.txt /tmp/requirements.txt
RUN cd /tmp && pip install -r requirements.txt

# Create the project directory
RUN mkdir /learn
WORKDIR /learn
COPY learn /learn

EXPOSE 8000
USER uwsgi

COPY cmd.sh /
CMD ["/cmd.sh"]


