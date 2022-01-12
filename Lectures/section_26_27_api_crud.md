<!--
// cSpell:ignore pythonanywhere Postgre pypyodbc venv startproject asgi wsgi startapp djangorestframework psycopg2 countriesdb
-->

[previous](section_23_25_git_django.md.md)\
[main](../README.md)

## Building an Api From Scratch

<!-- <details> -->
<summary>
//TODO: add Summary
</summary>

### What is an API

Api Application programing interface, a set of specification for how programs interact with one another.

### Creating and activating a virtual environment

another case where we need a virtual environment.

```sh
mkdir project
python -m venv env_name
env_name\scripts\activate.sh

deactivate
```

### Installing Django and Django REST Framework

while we are inside the virtual environment.
(only works for me when i am in the windows console, not even powershell)

```sh
python -m pip install django
python -m django --version
python -m pip install djangorestframework
```

### Creating a new Django project and app

```sh
django-admin.py startproject worldCountries .
ls worldCountries
python manage.py startapp countries
ls countries
```

the project folder has:

- manage.py
- asgi.py
- settings.py
- urls.py
- wsgi.py

the app folder has

- migration folder
- python init file
- admin.py
- models.py
- tests.py
- views.py

### Register app with Django

we go to the settings.py file and we add the apps we installed to the **INSTALLED_APPS** list in the file.

we also add something to the middleware lists

### installing PostgreSQL Database Server

going to [postgresql website](https://www.postgresql.org/) and downloading the file

(or using a [docker](https://hub.docker.com/_/postgres))

we need to decide on a password and a port to use.

```sh
docker container run --name some-postgres -e POSTGRES_PASSWORD=<password> -d postgres
```

### Django and PostgreSQL Database Setup

we need the postgres installed, a running database, and the **Psycopg2** package installed. we need to configure the database setting inside the **settings.py** file of our project.

inside postgreSQL

- create new data

```sh
python -m pip instal psycopg2
```

setting.py file. before:

```py
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite',
        'NAME': os.path.join(BASE_DIR,'dn.sqlite3'),
    }
}
```

setting.py file. after:

```py
DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME': 'countriesdb',
        'USER': 'postgres'
        'PASSWORD': #some password
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

### Running initial migration

### Creating a Django Model

### Creating and applying new migration

### Creating a serializer class

### Starting and stopping Django development server

### Creating a superuser account

### Creating views : part 1

### Creating views : part 2

### Mapping views to URL

### Register model with admin site

### Creating model objects

### Installing Postman

### Testing API

</details>

## Creating A Crud App

<!-- <details> -->
<summary>
//TODO: add Summary
</summary>

### What is CRUD

### What we will create

### Application design|sketch

### Create Project directory and Python File

### Creating app GUI: Part 1

### Creating app GUI: Part 2

### Creating app GUI: Part 3

### Creating app GUI: Part 4

### Creating app GUI: Part 5

### Adding comments to your code

### Please Note

### What is SQL Server

### Minimum Installation Requirements for SQL Server 2019

### SQL Server Editions

### Download SQL Server Developer Edition

### Install SQL Server Developer Edition

### Install SSMS

### Connecting to SQL Server with SSMS

### Creating a database and table

### Creating a database configuration file

### Create a virtual environment and install pypyodbc

### Connect python file to database

### Create a cursor object

### Create a class and methods

### Add more methods to class

### Create function for selected row

### Create more functions

### Activate button widgets

### App and database interaction: Part 1

### App and database interaction: Part 2

<details>

[next]()
