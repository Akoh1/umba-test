# A Mock Audio Server API


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



### Run migrations before starting the flask-server

#### Set up and configure database with the parameters in the DATABASE_URL in the config.py
#### or adjust to fit your own database details before proceeding to the next steps

```python
   python manage.py db init
```

```python
   python manage.py db migrate
```

```python
   python manage.py db upgrade
```

```python
   python manage.py runserver
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




