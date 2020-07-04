# Django REST API
##### Basically the project I'm teching some diploma students. They can't find out `Django` teacher.
## Setup

### Dependancies

- Python 3.6.9 
- Django 3.0
- Mysql 8.0.19


### Create Database
The roject I'm using MySql database. If you would use to `mysql`database you should follow the `command` 

First you install `mysql` on your Machine/operating system. Here I don't explain `how to install mysql?` in your system.

<h2>How to create mysql database</h2>
First go to your terminal then follow the command line
```
mysql -u root -password
create dataase db_name;
```

Create a python virtual environment:

```bash/zsh
virtualenv venv --python=python3.6
```

Activate it:

```bash/zsh
source env/bin/activate
```

```
pip install -r requirements.txt

python3 manage.py runserver # or
./manage.py runserver
```

If you use `mysql` in your another project must be install mysql-client
`pip install mysqlclient`

