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














