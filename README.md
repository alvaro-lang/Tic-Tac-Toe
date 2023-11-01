# Tic_Tac_Toe project
Project made in python 3.

Add to the project a virtualenv and install the dependencies of requirements.txt file. Also, add enviroment variables from .env.example file to your .env file

## Steps

Install pip packages in virtualenv from the file requirements.txt
```
pip install -r "requirements.txt"
```

Run the server
```
python manage.py runserver
```

Make migrations to sqlite database
```
python manage.py makemigrations
```
```
python manage.py migrate
```