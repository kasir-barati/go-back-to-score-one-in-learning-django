# Where you can find the course?

- https://www.dj4e.com/

# What motivates me to learn it?

- TBH I am - Right now, 2022-07-02 - looking for a good opportunity in Germany. And so I am a Node.js developer. So I decided to learn what seems to be in demand
- But now I am really inspired and fascinated about python and I can say I swept of my feet :joy:

# What is going on here?

- I captured the my learning process in this repo and TBH I think I will go even further and I will create a powerful repo on top of this beautiful free course which is really doable almost I think for everyone as it is named
- I did some changes as I like so please do not expect this be the same way as it is done in the course
- When we just say `pip` or `python` it means that we wanna use python version 3

# Install Django

- `pip install -r requirements.txt` to install dependencies
- A bunch of command related to `manage.py`
  - Automatically created.
  - `python manage.py <command> [options]`
    - Available commands:
      - **auth**
        - changepassword
        - createsuperuser
      - **contenttypes**
        - remove_stale_contenttypes
      - **django**
        - `check`: Inspect the entire Django project for common problems.
        - compilemessages
        - createcachetable
        - dbshell
        - diffsettings
        - dumpdata
        - flush
        - inspectdb
        - loaddata
        - makemessages
        - `makemigrations`: Creates new migrations based on the changes detected to your models.
        - `migrate`: to apply created migrations
        - sendtestemail
        - shell
        - showmigrations
        - sqlflush
        - sqlmigrate
        - sqlsequencereset
        - squashmigrations
        - `startapp` to create a new app (or module) with some boilerplate
        - startproject
        - test
        - testserver
      - **rest_framework**
        - generateschema
      - **sessions**
        - clearsessions
      - **staticfiles**
        - collectstatic
        - findstatic
        - `runserver`: to start your app
    - Available options:
      - `--verbosity` To log more in terminal
      - `--deploy` to do some extra check in deploy mode
      - ``

1. `mkdir d4e`
2. `cd d3e`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install django`

- Now you can create a new project:
  - `django-admin startproject go_back_start_again`
    - `django-admin` is a command-line utility for administrative tasks.

# `settings.py`

- `ALLOWED_HOSTS` tells Django to make our app available for which host/domain name. It is basically an array of strings
