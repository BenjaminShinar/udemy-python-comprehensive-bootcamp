<!--
// cSpell:ignore scrapy beautifulsoup aquote Virtualenv urlopen urllib startproject middlewares aciobanu runspider pinterest disqus mahalo wsgi runserver stopserver makemigrations sqlmigrate showmigrations startapp actiontasks contenttypes staticfiles createssuperuser todolist urlpatterns varchar
-->

[previous](section_17_19_exceptions_projects_gui.md)\
[main](../README.md)

## Section 20: Web Scraping

<details>
<summary>
Scraping websites from Data
</summary>

web harvesting, web data extraction, downloading information from websites and analyzing it. used for indexing websites, online shopping (finding the best price) or getting product reviews.

basic rules:

- check the website terms and conditions to avoid legal issues.
- don't be too aggressive (too many calls can count as DOS attack).
- check the layout of the site and adapt the code to it.

### Tools for Web Scraping

some popular tools:

- scrapy - open source tool, used for crawling web sites and extracting structured data.\
  `pip install Scrapy`

- beautiful soup. a python library for getting data from HTML and XML files\
  `pip instal beautifulsoup4` (bs4)

### What we will Scrape

in this course we will practice by scraping a [quotes website](https://bluelimelearning.github.io/my-fav-quotes)

website is down. but here is how the html looks like (one quote only).

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>My Favorite Quotes</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>Words of Wisdom</h1>
    <div id="wrapper">
      <div class="quotes">
        <p class="aquote">
          I hear and I forget.<br />I see and I remember.<br />I do and i
          understand.
        </p>
        <p class="author">Confucius</p>
      </div>
    </div>
  </body>
</html>
```

### Virtual Environment

when we install python, it's installed globally, but we might want to install different packages per project. this can be done with a virtual environment (or a container!). we can create a virtual environment with the **Virtualenv** tool.

we create a directory and go into it, and then we make sure we have the package installed

```sh
mkdir new_env
cd new_env
pip show virtualenv
pip install virtualenv
virtualenv <env_name>
<env_name>\scripts\activate #activate
<env_name>\scripts\deactivate #activate
```

**when we activate the virtual environment, the prompt should change to the environment name.**

(I'm using a dockerfile, because it's easier for me to do so.)

### Installing Beautiful Soup

we can install beautiful soup inside the virtual environment (or in the docker image)

```sh
pip install beautifulsoup4
```

now we can import the package in our python code.

### Prototyping the Script

this comes before the script itself. the videos are in a bad order.

the **urllib** package has the **request** object and the _read()_ function.

we start with the python shell, this way we can always go back and change stuff or look at our variables.
we could probably just take the html from the file itself without the request or the client.

```py
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_page = "https://bluelimelearning.github.io/my-fav-quotes"

url_client = uReq(quotes_page)
website_data = url_client.read()
url_client.close()
page_soup = soup(page_html,"html.parser")
quotes = page_soup.findAll("div",{"class":"quotes"}) #name, attributes
len(quotes)
quotes[0].text #just the text
page_soup.h1 #h1 elements
page_soup.h1.text.strip() #h1 elements text
```

### Build a Web Scrapping Script

we can start building our app at last.

we import what we need from the packages, and then we define the html page which we want to scrape.

```py
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

quotes_page = "https://bluelimelearning.github.io/my-fav-quotes"

def scrape(page):
    with uReq(page) as uClient:
        page_html = uClient.read()
    page_soup = soup(page_html,"html.parser")
    return page_soup

def getQuotes(soupPage):
    quotes = soupPage.findAll("div",{"class":"quotes"})
    return quotes

page = scrape(quotes_page)
quotes = getQuotes(page)
print(len(quotes))
print(quotes)
```

**I had to play around a lot with nginx to make this work. it was a mess**

### Testing and Saving Scraped Data

this continues the python script.

we redirect the output of the script to a file.

```sh
python scrape_quotes.py > quotes.text
```

### Installing Scrapy

now we will use Scrapy to scrape web pages.
we can install it inside the virtual environment

```sh
python pip install Scrapy
```

### Creating a Scrapy Project

[Scrapy on docker hub](https://github.com/aciobanu/docker-scrapy)

we need a new scrapy project, so we move to the directory

```sh
mkdir scraping
cd scraping
Scrapy startproject <projectName> .
#docker
docker container run --rm -v $(pwd) aciobanu/scrapy startproject Scrapy
```

this creates a default scrappy project.
it has the project directory and the _scrapy.cfg_ configuration file and other files inside the project

- \_\_init\_\_.py
- items.py
- middlewares.py
- pipelines.py
- settings.py
- spiders (folder)

### Scrapy Architecture

how the data flow works in Scrapy.

there is an engine that controls everything, a spider asks the engine to crawl a website, and it schedules a search. a scheduler receives the requests and manages the requests to the engine. there is a downloader and a downloader middleware. the spiders process the response and return the parsed objects to the engine. the items are sent to the item pipeline, which further process them.

### Creating a Spider

spiders are classes that Scrapy uses to scrape with. spiders must derive from the **scrapy.Spider** class and must define the initial request they make.

we must give it a name, which urls it scrapes and how it parses them. we don't need to create a constructor because we don't add anything to the object instance.

scrapy uses selectors (just like other languages), the same selectors we use with CSS, (also something called Xpath)

[CSS selectors](https://www.w3schools.com/cssref/css_selectors.asp)

we also use the _yield_ keyword to return the item from generator.

```py
import scrapy

class QuotesSpider(scrapy.Spider):
    name= "quote"
    start_urls =["https://bluelimelearning.github.io/my-fav-quotes"]


    def parse(self,response):
        for quote in response.css("div.quotes"): #div elements with the quotes class
            yield {
                "quote":quote.css("p.aquote::text").extract(),
                "author":quote.css("p.author::text").extract_first(),
            }
```

### Scraping Data with Scrapy Shell

an interactive shell to debug scraping

[Scrapy documentation](https://docs.scrapy.org/en/latest/topics/shell.html)

i used a docker file

```sh
Scrapy shell <some website>

docker container run --rm -ti  aciobanu/scrapy shell
```

now we can start scraping from the shell

```
fetch("https://bluelimelearning.github.io/my-fav-quotes")
response
response.css("title")
response.css("title::text").extract()
response.css('head')
quote =response.css('div'.quotes")[0]
exit()
```

### Running the Spider

to run a spider we move to the directory with with the spider and run a command. we can determine what format we wish to save the data to, we can use xml, json or csv.

```sh
cd scrapy/spiders
scrapy runspider quotes_spider.py -o quotes.xml
```

</details>

## Section 21: Django Basics

<details>
<summary>
The basics of Django and web development
</summary>

[Django](https://www.djangoproject.com/) is an open source web application written in python. a web framework is a collection of tools and components to create websites. it is not a programming language.

django was used to build websites and programs such as:

- Instagram
- Pinterest
- The Onion
- Disqus
- Mahalo
- Nasa
- and many more, see [Django Sites](https://djangosites.org/)

### Django Architecture

django uses mvc architecture, model-view-controller. but with four parts and different names

- URL Patterns - request path, direct the request to a view.
- Views - a logic layer, take a request a returns a response.
- Models - the data itself.
- Templates - how the data is displayed.

### Creating Project Directory

we create a directory for the project
[try here](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/)
or [here](https://docs.docker.com/samples/django/)

```sh
.\env\Scripts\activate
pip install django==3.2.6
env\Scripts\django-admin.exe startproject .
python todoApp\manage.py migrate
python todoApp\manage.py runserver
echo "Django==3.2.6" > requirements.txt #remove quotes
env\Scripts\deactivate
del env
```

### Django App vs Django Project

a django project is not the same as a django app. an app is a web application that does something. a project is a collection of configurations and apps that make up a website. one project can use many apps, and the same app can be used in many projects.

</details>

## Section 22: Building a Web App with Django

<details>
<summary>
Creating a Django App - not really operational
</summary>

We will create a basic 'todo' app that we can add items to it, delete items and mark as completed.

### Creating a Django Project

we can run the same command with or without the period. if we add the period then it will be built directly, otherwise, there will be another extra container period.

```sh
django-admin startproject <project name>
django-admin startproject <project name> .
```

### Anatomy of a Django Project

- \_\_init\_\_.py - empty fle the makes the folder a package
- settings.py - configuration
- urls.py - manages the entry points, which apis are available.
- wsgi.py - development server, serves the project
- _manage.py_ - a command line utility to interact with the server

### Starting and Stopping Django Development Server

just checking that things work

we need to be inside the virtual environment, the default port is 8000

```sh
python manage.py runserver
python manage.py runserver <port>
python manage.py stopserver <port>
```

we might see that we have migration problems, which somehow relates to databases.

### Django Migrations

migrations is propagating changes from the model into the database schema.

migration commands
Command | Description
---|---
`migrate` | applies and un-applies migrations
`makemigrations`| create a new migration based on changes to the model
`sqlmigrate` | displays the sql statements for a migration
`showmigrations` | list migrations

so if we want to see migrations that are still waiting to happen. if there are, we migrate them and check again.

```sh
python manage.py showmigrations
python manage.py migrate
python manage.py showmigrations
```

### Installing Django App

each app has the same structure, apps should be named as plural.

```sh
django-admin startapp jobs
```

or with my docker configuration...

```sh
docker-compose up -d --build
docker-compose exec web python manage.py startapp actiontasks
docker-compose down
```

we need to activate the app by adding it to the settings.py file.

we find the **INSTALLED_APPS** list inside the file and add our app to it.

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'actiontasks',
]
```

### Anatomy of a Django App

the autogenerated components of the django app.

- _migrations_ folder - tracking database changes
- python init file
- _admin.py_ - register models here
- _apps.py_ - configurations
- _models.py_ - data and behavior
- _tests.py_ - unit test
- _views.py_ - view functions

### Django admin and superuser

when you install django, the project comes with a administrative interface page, so we create a appropriate super-user to interact with the website.

```sh
python manage.py createssuperuser
python manage.py runserver
```

we go to the site and add "/admin" to the web address and we can log-in to the administrative console.

### Django Templates

Templates have static parts of html, special syntax for dynamic content

```django
{ % tag % }
{{ variable }}
{{ variable | filter}}
```

in the app directory, we create a folder called "templates", and inside it a folder with the app's name, and there we add the "index.html" files.
we also have a similar structure starting with "static", which includes a folder with the app name, and inside that folder, we add the css files and the boot strap files

> - app_name\templates\app_name\index.html
> - app_name\static\app_name\style.css

### Django Views

views take a web response and return a response (such ash html. xml, a redirect, etc...). the view contains the logic to return the response.

the convention is to stick all the views in the views.py file.

```py
from django.shortcuts import render

def index(request):
  return render(request,"app/index.html") #template to use
```

### URL and URL Patterns

url stands for **uniform resource locator** django url patterns contains the path of the url and where to send it.

in the "urls.py" file, we match the url patterns from a path to a behavior, we can define a redirect to another url pattern file.

```py
from django.contrib import admin
from django.urls import path,include

urlpatterns= [
  path('admin/', admin.site.urls),
  path('',include("todolist.urls"))
]
```

now lets create a python file called "urls.py" in the app folder and add stuff there. we define the url pattern to use the logic in the views file.

```py
from django.urls import path
from . import view

urlpatterns = [
  path("", views.index,name="index")
]
```

### Accessing static files

static files are the css and boot strapping files, we can reference them from the html with special syntax

```html
{% load static %} <!DOCTYPE html>}
<html lang="en">
  <head>
    <link
      rel="stylesheet"
      href="{% static 'todolist/bs/css/flatly.min.css' %}"
    />
    <link rel="stylesheet" href="{% static 'todolist/styles.css' %}" />
  </head>
</html>
```

### Django Models

models are how data is stored in the database, each object is a row in a table, the model is the source of truth for the folder. each model is a python classes which is derived from **django.db.models.Model**.

```py
from django.db import models

class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
```

is equivalent to the sql command to create a table.

```sql
CCREATE TABLE my_app_person(
  "id" serial NOT NULL PRIMARY KEY,
  "first_name" varchar(30) NOT NULL,
  "last_name" varchar(30) NOT NULL,
);
```

### Creating a Model

a model is a schema for the database, we go to the app directory and the _model.py_ file

```py
from django.db import models

class Todolist(models.Model):
  taskDesc = models.CharField(max_length=45)
  taskCompleted = models.BooleanField(default=False)

  def __str__(self):
    return self.text
```

### Migrating Models

wee add the python classes in the models.py folder to the database.

```sh
python manage.py makemigrations
python manage.py migrate #create the table
```

### Adding Models to Admin Site

```sh
python manage.py runserver
```

log in into the site.

we now register the model, we go the the _admin.py_ file

```py
from django.contrib import admin

from .models import TodoList

admin.site.register(Todolist)
```

now we can refresh the site and add the model to the site, we can now create items from the administrative page.

</details>

[next](section_23_25_git_django.md)
