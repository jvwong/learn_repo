# Learn Project

## Docker 

### Use Compose to build the image
```
 $ docker-compose build
```
This instructs Compose to build webapp. 

```
 $ docker-compose up
```

This runs the app.

## Create the database 
With the container ('learnrepo_db_1') running, create the database:
``` 
 $ docker exec learnrepo_db_1 createdb -Upostgres learn.db        
```

## Create Super User
With the container ('learnrepo_learn_1') running, make the initial migrations: 

```
 $ docker exec learnrepo_learn_1 python manage.py makemigrations
 $ docker exec learnrepo_learn_1 python manage.py migrate 
```

Now create a super user:
```
 $ docker exec -it learnrepo_learn_1 /bin/bash    
 root@:/learn# python manage.py createsuperuser
 ...
 root@:/learn# exit
```

