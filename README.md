# Django Restful Api
A todoapp using django rest framework for both front-end and back-end.

- User Auth. with jwt
- Forget password future added.
- Users can do CRUD operations on Task model.
- Application is dockerized. Using docker-compose and dockerfile.

# Environment Setup
Follow these steps to be sure your environment is acceptable for the project. I assume that you have docker installed in your system.
- Create env file using any library for python.
    - `python -m venv my-env`
    - `. my-env/bin/activate`
- Then install libraries in requirements.txt
    - `pip install -r requirements.txt`
- Create .env file with these values:
    - DB_NAME, DB_USER, DB_PASS
- Create init.sql file to initalize your sql database for docker. 
    - CREATE TABLE IF NOT EXIST `yourdb_name`
- Thats it! Sit back and enjoy docker magic after running these command:
    - `docker-compose up`

# Api Schema
- Created basic api schema.

![api](https://i.ibb.co/5nJzvdb/UML-API-diagram-todoapp.png)


# Home Page

![anasayfa](https://i.ibb.co/FJ160D3/updatedproject.png)


