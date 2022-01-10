<!--
// cSpell:ignore pycache todolist endfor describeby urlpatterns
-->

[previous](section_20_22_web_scraping_django.md)\
[main](../README.md)

## Section 23: Version Control

<details>
<summary>
Git and Version Control
</summary>

### What is Git

version control record changes to files over time. git is distributed, it's not dependant on a single source, it's used in both big and small projects.

git runs on a command line, git uses repositories to track changes. it can be used by a team and keep a record of changes.

### What is Github

github is a web based git repository hosting service. it has a graphical interface to look through repositories and branches, it also provides tools like tracking tasks and bugs, it's the largest host of source code.

### Installing Git

```sh
sudo apt-get install git

```

### Git Configuration

when we change the git configurations, we can do it one on of the three levels:

- system level configurations
- user level configurations
- repository level configurations

```sh
git config --system
git config --global #user
git config --local #default behavior
git config --worktree
```

so for example, we can set the user name and email

```sh
git config --global user.name "benjamin"
git config --local user.email "abc@gmail.com"

git config --system --list
git config --global --list
git config --local --list
```

### Creating Github Account

go to the website and do the thing.

### Initializing git repository

```sh
git init
ls .git
```

### Adding files and Excluding files From Version Control

the _.gitignore_ file stores which files won't be uploaded to the repository, we won't track the the virtual environment, for example.

so we simply add the path of the files into the .gitignore file.

```sh
git status
git add . #add everything
git status
git rm -r --cached myLst/__pycache__
echo "__pycache__" >> .gitignore
git status
```

adding means taking files into the staging file, this is still before committing them to version control.

the next step is to commit the files, which means making a snapshot of the status of the repository

```sh
git commit -m "message!"
```

### Using a Remote Repository

we need a repository in github.

```sh
git remote -v
git remote add origin https://github.com/username/repositroy.git
git remote -v
git push -u origin master # upstream remote repo and branch
git status
```

</details>

## Section 24: Implementing Dynamic Data Display

<!-- <details> -->
<summary>
//TODO: add Summary
</summary>

Back to the django application

### Displaying Data from Database

we want our website to use the database to pull data into dynamic display.

we look at the views.py file,

```py
from  django.shortcuts import render
from .models import TodoList

def index(request):
    todo_items = TodoList.objects.order_by(id) #from the app database
    context = {'todo_items':todo_Items}
    return render(request, 'todolist/index.html',context)
```

now we update the html

```html
<ul class="list-group t20">
  {% for todolist in todo_items &}
  <li class="list-group-item">{{todolist.text}}</li>
  {% endfor %}
</ul>
```

### Setting Background Color for Completed Items

modifying the html to add classes, we use the `{% %}` syntax.

```html
<ul class="list-group t20">
  {% for todolist in todo_items &} {% if todolist.completed %}
  <li class="list-group-item todo-completed">{{todolist.text}}</li>
  {% else %}
  <a href="#"><li class="list-group-item">{{todolist.text}}</li></a>
  {% endif %} {% endfor %}
</ul>
```

### Adding a form

having something that can add tasks

we start with a hard coded form

```html
<form action="#" method="POST" role="form">
  <div class="form-group">
    <div class="input-group">
      <input type="text" class="input-form-control" placeholder="Enter task" />
      <span class="input-button">
        <button type="submit" class="btn btn-default" id="add-btn">ADD</button>
      </span>
    </div>
  </div>
</form>
```

we create a python files forms.py

```py
from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45, widget=forms.TextInput(
        attrs={'class': 'form-control',
        'placeholder': 'ender task',
        'aria-label': 'Todo',
        'aria-describeby':'add-btn'}))
```

with this we can Capture the data from the form, we go back to the views.py file. we add the form to the index page and redirect from the post back to the main page. we also use a decorator.

```py
from  django.shortcuts import render,redirect
from .models import TodoList
from .forms import TodoListFrom
from django.views.decorators.http import require_POST

def index(request):
    todo_items = TodoList.objects.order_by(id) #from the app database
    form = TodoListForm()
    context = {'todo_items':todo_Items, 'form':form}
    return render(request, 'todolist/index.html',context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    return redirect('index') #send to the index
```

we also update the url pattern

```py
from .django.urls import path
from . import views

urlpatterns = [
    path('', view.index, name='index'),
    path('add', view.addTodoItem, name='add'),
]
```

and we finally update the html

csrf = cross site request forgery

```html
<form action="{% url 'add' %}" method="POST" role="form">
  {% csrf_token %}
  <div class="form-group">
    <div class="input-group">
      {{ form.text }}
      <span class="input-button">
        <button type="submit" class="btn btn-default" id="add-btn">ADD</button>
      </span>
    </div>
  </div>
</form>
```

### Adding Form Input to Database

continuing with the views.py file.

```py
from  django.shortcuts import render,redirect
from .models import TodoList
from .forms import TodoListFrom
from django.views.decorators.http import require_POST

def index(request):
    todo_items = TodoList.objects.order_by(id) #from the app database
    form = TodoListForm()
    context = {'todo_items':todo_Items, 'form':form}
    return render(request, 'todolist/index.html',context)

@require_POST
def addTodoItem(request):
    form = TodoListForm(request.POST)
    # print(request.POST['text']) #log to console
    if form.is_valid():
        new_todo = TodoList(text=request.POST['text'])
        new_todo.save()
    return redirect('index') #send to the index page
```

### Creating a view for completed items

### Creating a view to delete all completed items

### Creating a view to remove all items from database

### Pushing updates to version control

</details>
