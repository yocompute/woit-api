# woit-api
woit-api is a django backend for angular 2.x/ionic website template


## Requirement
python 2.7 or python 3.4
django 1.10 or 1.11

## Set up with virtualenv (Optional)
### Install virtualenv
Install virtual env
```
> pip install virtualenv
```

activate virtual env (Windows):
```
> cd woit-api
> virtualenv woit_env
> woit_env/Scripts/activate.bat
```

activate virtual env (Linux/Mac):
```
> cd woit-api
> virtualenv woit_env
> . woit_env/bin/activate
```


Deactivate virtual env (Windows):
```
> woit_env/Scripts/deactivate.bat
```

Deactivate virtual env (Linux/Mac):
```
> . woit_env/bin/deactivate
```

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

### Install mysql python connector
Go to Oracle official and download connector and install

### Install mysqlclient python with wheel (If you cannot install with pip install)
After install the oracle mysql connector, use pip to install mysqlclient
```
> pip install mysqlclient
```


### Add a woit.config.json with your mysql credential
Create a woit.config.json file, change username and password of your mysql and place under the woit-api's parent folder with following content:
```
{
	"ENV": "local",
	"DATABASE":{
		"USERNAME":"mydbuser",
		"PASSWORD":"mydbpass"
	}
}
```


### Migrate Django tables
```
> cd woit-api
> python manage.py makemigrations
> python manage.py migrate
```

### Create Django admin superuser 'admin'
```
> python manage.py createsuperuser --username admin
```

### Start
```
> cd woit-api
> python manage.py runserver
```

Open a browser, type http://localhost:8000/items in address bar, you will see [] in your browser.
Open a browser, type http://localhost:8000/admin in address bar, and use admin credential you just created to login admin page.




