# An app based on DRF Tutorial
[Link to tutorial 1](https://www.django-rest-framework.org/tutorial/1-serialization/)

## Development setup
Install Python 3.7.2

## Create a virtual environment:
`python3 -m venv venv`

## Activate a venv:
`source venv/bin/activate`

## Install dependencies:
`pip install -r requirements.txt`

## Migrate db:
`python3 manage.py makemigrations` <br/>
`python3 manage.py migrate`

## Create an admin account:
`python manage.py createsuperuser`