### Introduction
Task Manager built in Python, Flask and SQLLite. 

### Instalation

[Download and install Python3](https://www.python.org/downloads)
Check python installed version:
```shell
python --version
```

Install virtual env:
```shell
pip install virtualenv
```
virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Create a virtual environment:
```shell
virtualenv env
```

Select the environment:
If you are using Visual Code IDE:
- Open the terminal view inside Visual Code (Ctrl + ç - Portuguese Keyboard)
- Choose the GitBash as default bash
- Execute the command bellow

```shell
source env/Scripts/activate
```

Install required libs:
```shell
pip install flask flask-sqlalchemy
```

Create the SQL Lite database

1 - Access python console:
```shell
python
```

2 - Connect to the Sqlite:
```shell
from app import db
```

3 - Create the SQLite database:
```shell
db.create_all()
```

### Run

To start the Flask server:
```shell
python app.py
```

To check the basic URL created:
```
http://localhost:5000/
```

### WSGI - Web Server Gateway Interface

Web Server Gateway Interface and it's a spec for a software interface between a web server and a python application.
- [Introduction into the WSGI ecosystem](https://www.ultravioletsoftware.com/single-post/2017/03/23/An-introduction-into-the-WSGI-ecosystem)
- [Using Nginx for Production ready Flask app with uWSGI](https://medium.com/@ksashok/using-nginx-for-production-ready-flask-app-with-uwsgi-9da95d8ac0f9)

### Gunicorn: WSGI HTTP Server used to scale Flask workers (Similar to uWSGI implemented in this project)

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy

- [Gunicorn](https://gunicorn.org/)
- [Deploy a Python Flask Restful API app with gunicorn, supervisor and nginx](https://medium.com/@thucnc/deploy-a-python-flask-restful-api-app-with-gunicorn-supervisor-and-nginx-62b20d62691f)

### Celery: Distributed Task Queue
Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.

The execution units, called tasks, are executed concurrently on a single or more worker servers using multiprocessing, Eventlet, or gevent. Tasks can execute asynchronously (in the background) or synchronously (wait until ready).
- [Celery](http://www.celeryproject.org/)
