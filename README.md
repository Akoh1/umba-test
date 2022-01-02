# Umba test


## Getting started

Steps:

1. Clone/pull/download this repository
- You'll need to have virtual enviroment installed on your machine  

    ```python
  pip3 install virtualenv
  
    ```


- Setup virtual environment

    ```markdown
    virtualenv -p python3 env
    
    ``` 

- Activate virtual environment

    ```markdown
    source env/bin/activate
    
    ```
    

   - Install requirements
    
        ```bash
        pip install -r requirements.txt
        ```

## Seed Database from user api profile
### Run seed.py to create database and upload user data from api to database:
```python
   python seed.py
```
### Run with parameters to set number of users to be uploaded to the database

```python
   python seed.py -t/--total <total>
```
### Run flask-server
   To run flask server:
   ```python
      python manage.py runserver
   ```

   ### This application uses the seed script to create a user table in an sqlite database 
   ### and fetch user data from an api url to insert into the user table.
   ### The application fetches these user data from the user database onto the users views

### Normal flask migration functions for creating database in models
   Add your models to models.py and run the migrations to use them in database
   NB: Running this will remove the users table added by the seed.py script from the database
   as it will not be part of the migrations script generated, so add the to migrations 
   if you want to keep users table in database

   ```python
      python manage.py db init
   ```

   ```python
      python manage.py db migrate
   ```

   ```python
      python manage.py db upgrade
   ```







