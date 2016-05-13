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
With the container ('learnrepo_db_1') running, get a terminal connected to it:
``` 
 $ docker exec -it learnrepo_db_1 /bin/bash    
```

Now create the database:
```
 root@:/# createdb -Upostgres learn.db
 root@:/# exit       
```

## Create Super User
With the container ('learnrepo_learn_1') running, get a terminal connected to it: 

```
 $ docker exec -it learnrepo_learn_1 /bin/bash    
```

Now create a super user:
```
 root@:/learn# python manage.py makemigrations 
 root@:/learn# python manage.py migrate
 root@:/learn# python manage.py createsuperuser
 ...
 root@:/learn# exit
```

