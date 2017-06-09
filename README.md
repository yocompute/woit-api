# woit-api
woit-api is a python 2.7 django backend for angular 1.x website template

## Quick setup

### Download python plugins
```
> pip install -r requirements.txt
```

### Install mysql and create datase
Install mysql and open a shell:
```
mysql> CREATE DATABASE woit CHARACTER SET utf8 COLLATE utf8_general_ci;
```

### Create mysql account 'dbuser'/mypasswd:
```
mysql> CREATE USER 'dbuser'@'localhost' IDENTIFIED BY 'mypasswd';
mysql> GRANT ALL PRIVILEGES ON * . * TO 'dbuser'@'localhost';
mysql> FLUSH PRIVILEGES;
```

### Install mysql python 2.7 connector

### Install mysqlclient python 2.7 with wheel (If you cannot install with pip install)

### Migrate Django tables
```
> cd woit
> python manage.py makemigrations items
> python manage.py migrate
```

### Create Django admin superuser 'admin'
```
> python manage.py createsuperuser --username admin
```

### Start
```
> cd woit
> python manage.py runserver
```

Open a browser, type http://localhost:8000/items in address bar, you will see [] in your browser.
Open a browser, type http://localhost:8000/admin in address bar, and use admin credential you just created to login admin page.


## Set up with virtualenv (Optional)
### Install virtualenv
Windows:
Inactivate virtual env:
```
> cd woit
> virtualenv woit_env
> woit_env/Scripts/activate.bat
```

Deactivate:
```
> woit_env/Scripts/deactivate.bat
```
### Download python plugins
```
> pip install -r requirements.txt
```

