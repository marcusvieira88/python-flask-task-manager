### Introduction
Task Manager built in Python, Flask and SQLLite. 

### Instalation

[Download and install Python3](https://www.python.org/downloads)
Check python installed version:
´´´bash
python --version
´´´

Install virtual env:
´´´bash
pip install virtualenv
´´´
virtualenv is a tool to create isolated Python environments. virtualenv creates a folder which contains all the necessary executables to use the packages that a Python project would need.

Create a virtual environment:
´´´bash
virtualenv env
´´´

Select the environment:
If you are using Visual Code IDE:
- Open the terminal view inside Visual Code (Ctrl + ç - Portuguese Keyboard)
- Choose the GitBash as default bash
- Execute the command bellow

´´´bash
source env/Scripts/activate
´´´

Install required libs:
´´´bash
pip install flask flask-sqlalchemy
´´´

Create the SQL Lite database

1 - Access python console:
´´´bash
python
´´´

2 - Connect to the Sqlite:
´´´bash
from app import db
´´´

3 - Create the SQLite database:
´´´bash
db.create_all()
´´´

### Run

To start the Flask server:
´´´bash
python app.py
´´´

To check the basic URL created:
´´´
http://localhost:5000/
´´´














