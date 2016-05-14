# Learn Project

## Docker 

### Use Compose to build the image
```
 $ docker-compose run web python manage.py migrate
```
This instructs Compose to run ```python manage.py migrate``` in a container, using the web service’s image and configuration. Because the web image doesn’t exist yet, Compose builds it from the current directory, as specified by the build: . line in docker-compose.yml.

Once the web service image is built, Compose runs it and executes the ```python manage.py migrate``` command in the container. This command instructs Django to create the database models.


```
 $ docker-compose up
```

This runs the app.


## Create Super User
Now create a super user:
```
 $ docker exec -it learnrepo_learn_1 /bin/bash    
 root@:/learn# python manage.py createsuperuser
 ...
 root@:/learn# exit
```

