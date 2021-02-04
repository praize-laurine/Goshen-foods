## Project Name
Goshen-foods

## Description
This is a django application that allows users to order online.

## Setup and installations
- Fork the data onto your own personal repository. 
- Clone Project to your machine 
- Activate a virtual environment on terminal:
- <code> source virtual/bin/activate </code>
- Install all the requirements found in requirements file. 
- On your terminal run <code>python3.6 manage.py runserver</code> 
- Access the live site using the local host provided.

## Getting started
# Prerequisites
- <code>python3.6 virtual environment pip</code>

## Clone the Repo and rename it to suit your needs.
- https://github.com/praize-laurine/Goshen-foods

## Initialize git and add the remote repository
- git init
- git remote add origin <code>your-repository-url</code>

## Create and activate the virtual environment
- python3.6 -m virtualenv virtual<code>
- source virtual/bin/activate</code>

## Setting up environment variables
<pre><code>
DEBUG=True
DB_NAME='farm'
DB_USER=''
DB_PASSWORD=''
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
</code></pre>

## Install dependancies
- Install dependancies that will create an environment for the app to run<code> pip install -r requirements.txt</code>

## Make and run migrations
<pre><code>
python3.6 manage.py check
python manage.py makemigrations news
python3.6 manage.py sqlmigrate news 0001
python3.6 manage.py migrate
</code></pre>

## Run the app
<code>python3.7 manage.py runserver
</code>
## Built With
1. Python3.6
2. Django 3.1.6
3. Postgresql
4. Boostrap
5. HTML
6. CSS

## License
LICENSED UNDER License: MIT