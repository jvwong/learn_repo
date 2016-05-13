FROM python:3.5.1

RUN mkdir /learn
WORKDIR /learn
ADD requirements/base.txt /learn/

RUN pip install -r base.txt
COPY learn /learn

EXPOSE 8000

COPY cmd.sh /
CMD ["/cmd.sh"]

# docker rmi $(docker images -f "dangling=true" -q)
