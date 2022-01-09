<!--
// cSpell:ignore pycache
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

### Displaying Data from database

### Setting background color for completed items

### Committing changes to Github

### Adding a form

### Capturing data with form

### Adding form to template and view

### Adding form input to database

### Creating a view for completed items

### Creating a view to delete all completed items

### Creating a view to remove all items from database

### Pushing updates to version control

</details>
