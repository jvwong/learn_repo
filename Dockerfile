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

