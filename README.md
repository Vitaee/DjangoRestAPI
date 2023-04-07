# Django Restful Api
A simple todo app using django rest framework. For front-end html/css and ajax jquery used.

# Futures
- User Auth. with jwt
- Forget password functionally.
- CRUD operations on `Task Model`.
- Application is dockerized with `docker-compose.yml` and `Dockerfile`.

# My Development Environment
- Python version: 
``` 
Python 3.9.7 (default, Mar 11 2023, 23:46:23) 
[GCC 9.4.0] on linux
```
- Linux info:
```
Distributor ID: Zorin
Description:    Zorin OS 16.2
Release:        16
Codename:       focal
Linux vitae 5.16.0-051600-generic x86_64 GNU/Linux
```
# Environment Setup
Follow these steps to be sure your environment is acceptable for the project. I assume that you have docker installed in your system.
- Create env file using any library for python.
    - `python -m venv todo-env`
    - `. todo-env/bin/activate`
- Then install libraries in requirements.txt
    - `pip install -r requirements.txt`
- Create .env file with these values:
    - DB_NAME, DB_USER, DB_PASS
- Create init.sql file to initalize your sql database for docker. 
    - CREATE DATABASE IF NOT EXISTS `todo_dev`
- Thats it! Sit back and enjoy docker magic after running these command:
    - `docker-compose up`

# Api Schema
- Created basic api schema.

![api](https://i.ibb.co/5nJzvdb/UML-API-diagram-todoapp.png)


# Home Page

![anasayfa](https://i.ibb.co/FJ160D3/updatedproject.png)


