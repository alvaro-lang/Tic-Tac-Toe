# Tic_Tac_Toe project
Project made in python 3.

Add to the project a virtualenv and install the dependencies of requirements.txt file. Also, add enviroment variables from .env.example file to your .env file if is necessary.

It's implemented a sqlite database, so dont care about the database, it will be created automatically.

When you complete every step, execute the main.py file to start playing.

## Steps

Necessary package to create virtualenv
```
pip install virtualenv
```
Create virtualenv in project folder
```
virtualenv -p python3 <venv_name>
```
Enter virtualenv
```
source <venv_name>/bin/activate
```
Install pip packages in virtualenv from a file requirements
```
pip install -r "requirements.txt"
```
Create database
```
python manage.py migrate
```
Execute main.py
```
python main.py
```
