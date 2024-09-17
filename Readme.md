# Django Sample Project ASSIGNMENT

## Setup Guide
- Create a virtual environment
- Activate it
- Run `pip install -r requirements.txt`
- Config your database with your .env file OR create a postgres user with password `1234` and role name `postgres`
- Run `python manage.py migrate`
- Run `python manage.py runserver`
- Open your browser and head to http://localhost:8000/ship/upload/
- Upload your file
- Then you can check out other tabs on the page

## Tests
- There are tests in ship/tests that can be run using `python manage.py test`
