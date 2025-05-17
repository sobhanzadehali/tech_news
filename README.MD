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
