# woit
woit is a python 2.7 django backend for angular 1.x website template

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

Open a browser, you can issue command with http://localhost:8000/items, you will see [] in your browser.



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

