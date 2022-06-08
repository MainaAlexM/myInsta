# myInsta Clone
A photo sharing Social Media app for multiple users cloned from the Instagram App

A user can create an account, post, follow and comment on other people's posts while signed in.

## Live Link



## Set-Up and Installations

### Prerequisites
1. Linux Operating System
2. Python3.6 or latest
3. [Postgres](https://www.postgresql.org/download/) Database
4. Programming IDE e.g VS Code
5. python virtual environment

### Clone the Repo
Clone the repository by running the following command on the terminal:
`git clone git@github.com:Mathenge-Alex/myInsta.git`

### Activate the virtual environment
Activate virtual environment using python3
```bash
virtualenv -p /usr/bin/python3 venv && source venv/bin/activate
```

### Install dependancies
Install project dependencies with the command
`pip install -r requirements.txt`
This will install all the project pre-requisites.

### Create a local postgres database and connect with the project
```bash
psql
CREATE DATABASE instagram;
```
### .env file
Create an environment file .env, to store important credentials of the project. You can use the dummy set-up below to configure.
```python
SECRET_KEY = '<Secret_key>'
DBNAME = 'insta'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

# Cloudinary Credentials
CLOUD_NAME='<name>'
API_KEY='<key>'
API_SECRET='<secret>'
CLOUDINARY_URL='<url>'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '<your-email>'
EMAIL_HOST_PASSWORD = '<your-password>'
```
### Run Database Migration to Start up the Project
```bash
python3 manage.py makemigrations instagram
python3 manage.py migrate
```

### Create A Superuser
```bash
python3 manage.py createsuperuser
```
Configure the username, email and password as guided by the prompt.


### Run the app
```bash
python3 manage.py runserver
```
Open the local host address given on the terminal.
You should find your project running

## Known bugs
The project is unfinished.

## Technologies used
    - Git
    - Python
    - Postgresql
    - Javascript
    - HTML
    - Bootstrap 4
    - Heroku

### License
The project is governed by an MIT License
&copy Alex Mathenge 2022

