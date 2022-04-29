# Group 9's project: AVID
This is the fitness application for group 9's project, AVID. In here you will have all the necessary information 
to use it.
## Recommended IDE 
For this project, it's best to use Pycharm and have the latest version of Python.
## How to download the project in Pycharm.
- Click on the green button that says "Code", and then copy the HTTPS URL
- Once you open Pycharm for the first time, you have the option to use "get from VCS". Click on that
- Once you clicked on "get from VCS", paste the github URL and enter, Pycharm will create the program and adds a folder.
## Setting up a virtual environment 
- While in Pycharm, click on file, then settings
- Click on your project name and choose the python interpreter
- Download these necessary packages:
  - Django
  - django-crispy-forms
  - django-bootstrap4
  - pip

## How to run the program
- Make sure you delete db.sqlite3 first and delete every migration file except the ones that has "initial" in them
- Type python3 manage.py makemigrations in the terminal
- Type python3 manage.py migrate in the terminal
- Type python3 manage.py runserver in the terminal
- Click the development server
# You can now create an account and test the program's various functionality!
