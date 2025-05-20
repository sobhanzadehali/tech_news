<<<<<<< HEAD
# techNews
this project is a web application that allows users to read news articles from different sources.
is written in python and uses django framework and is only for educational purposes.

## requirements
listed in requirements.txt file.

## how to run
1. clone the project
2. cd into the project directory
3. run :
```bash
docker compose up
docker compose exec django sh -c "python manage.py migrate"
docker compose exec django sh -c "python manage.py createsuperuser"
docker compose exec django sh -c "python manage.py collectstatic"
```

## how to overview project
project apis have been documented using swagger.

go to http://localhost:8000/docs/swagger to see the documentation.

also you can go to localhost:5555/ to see celery flower dashboard 
=======
# techNews
this project is a web application that allows users to read news articles from different sources.
is written in python and uses django framework and is only for educational purposes.

## requirements
listed in requirements.txt file.

## how to run
1. clone the project
2. cd into the project directory
3. run :
```bash
docker compose up
docker compose exec django sh -c "python manage.py migrate"
docker compose exec django sh -c "python manage.py createsuperuser"
docker compose exec django sh -c "python manage.py collectstatic"
```

## how to view project
project apis have been documented using swagger.

go to http://localhost:8000/docs/swagger to see the documentation.

also you can go to localhost:5555/ to see celery flower dashboard 
>>>>>>> 26e4b6c0ccf132f96cdb39abba89a9c2bfe7867d
