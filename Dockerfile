FROM python:3.5.1

# Install dependencies
ADD requirements/base.txt /tmp/requirements.txt
RUN cd /tmp && pip install -r requirements.txt

# Create the project directory
RUN mkdir /learn
WORKDIR /learn
COPY learn /learn

# Apply database migrations
RUN python manage.py collectstatic --noinput

EXPOSE 8000

COPY cmd.sh /
CMD ["/cmd.sh"]

# docker rm $(docker ps -aq)

# Get rid of dangling images.
# docker rmi $(docker images -f "dangling=true" -q)

# Get rid of dangling volumes
# use docker 'rm -v' when deleting containers OR
# add the --rm flag with 'docker run'
# docker volume rm $(docker volume ls -fq dangling=true)
