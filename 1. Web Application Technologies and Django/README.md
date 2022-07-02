# Where you can find the course?

- https://www.dj4e.com/

# What motivates me to learn it?

- TBH I am - Right now, 2022-07-02 - looking for a good opportunity in Germany. And so I am a Node.js developer. So I decided to learn what seems to be in demand
- But now I am really inspired and fascinated about python and I can say I swept of my feet :joy:

# What is going on here?

- I captured the my learning process in this repo and TBH I think I will go even further and I will create a powerful repo on top of this beautiful free course which is really doable almost I think for everyone as it is named
- I did some changes as I like so please do not expect this be the same way as it is done in the course
- When we just say `pip` or `python` it means that we wanna use python version 3
- **DRF stands for Django REST Framework**

# CLI

- `pip install -r requirements.txt` to install dependencies
- `django-admin` is a command-line utility for administrative tasks.
- A bunch of command related to `manage.py`
  - Interact with this Django project
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
        - `startapp`
          - `python manage.py startapp polls`
          - A utility that automatically generates the basic directory structure of an app
          - Projects vs. apps:
            - App is a web application that does something.
            - A project is a collection of configuration and apps for a particular website.
        - `startproject` to create a new project
          - `django-admin startproject go_back_start_again`
          - Avoid naming projects after built-in Python or Django components.
          - What `startproject` created:
            - `manage.py`
            - `go_back_start_again/`:
              - root directory
            - `go_back_start_again/__init__.py`
              - Tells python to consider this directory as a Python package.
            - `go_back_start_again/settings.py`
              - Configuration for this Django project.
            - `go_back_start_again/urls.py`
              - URL declarations for this Django project
            - `go_back_start_again/asgi.py`
              - An entry-point for ASGI-compatible web servers to serve your project.
            - `go_back_start_again/wsgi.py`
              - An entry-point for WSGI-compatible web servers to serve your project.
        - test
        - testserver
      - **rest_framework**
        - generateschema
      - **sessions**
        - clearsessions
      - **staticfiles**
        - collectstatic
        - findstatic
        - `runserver`:
          - To start your app
          - Reload server automatically after you change something in codebase
            - Some actions do not cause restarting server, You have to stop and start it manually
              - One of them is adding new file
          - **Do not** use this server in anything resembling a production environment.
          - This command is tends to be only for dev env
          - Starts development server on the port 8000.
            - `python manage.py runserver 8080`
          - Starts the development server on the **internal network**
            - `python manage.py runserver 0:8000`
              - `0` is shorthand for `0.0.0.0`
    - Available options:
      - `--verbosity` To log more in terminal
      - `--deploy` to do some extra check in deploy mode
      - ``

# Steps I take in a glance

1. `mkdir d4e`
   - Put your code in some directory outside of the document root, such as `/home/mycode`.
2. `cd d3e`
3. `virtualenv venv`
4. `source venv/bin/activate`
5. `pip install django`
6. `django-admin startproject go_back_start_again`
7. `python manage.py startapp polls`

# `settings.py`

- `ALLOWED_HOSTS` tells Django to make our app available for which host/domain name. It is basically an array of strings

# Routing

- Point the root URLconf at the `polls.urls`, or whatever is the module's name.
  - `include('polls.url')`
    - Referencing other URLconfs.
    - Request comes, it chops off whatever part of the URL matched up to that point(Match to the defined string as endpoint) and sends the remaining string to the included URLconf(That newly created `polls/urls.py`) for further processing.
    - Reason behind the `include`:
      - Make it easy to plug-and-play URLs.
      - Since polls are in their own URLconf (`polls/urls.py`), they can be placed under `"/polls/"`, or under `"/fun_polls/"`, or under `"/content/polls/"`, or any other path root, and the app will still work.
        - TBH IDK what this section means
    - **You should always use `include()` when you include other URL patterns.**
      - `admin.site.urls` is the only exception to this.
  - `path()`
    - 4 arguments
      - 2 required:
        - `route`
          - A string that contains a URL pattern.
          - Django start from the first and goes down to the list
          - **Patterns don’t search `GET` and `POST` parameters**
            - I was stocked around 30min or I guess 1 hour on just this tiny data.
            - This is also right in DRF
          - **Patterns don’t search domain name.**
            - `https://www.example.com/myapp/`
            - `https://www.example.com/myapp/?page=3`
              - Both looks for URLconf `myapp/`
        - `view`
          - A matching pattern founded.
            - Call the specified view function with an `HttpRequest` object as the first argument
              - Any "captured" values from the route as keyword arguments.
      - 2 optional:
        - `kwargs`
          - Arbitrary keyword arguments can be passed in a dictionary to the target view
          - TBH IDK what it means
        - `name`
          - Naming your URL
          - Refer to URL unambiguously from elsewhere in Django
            - Redirect to another endpoint with their name
          - To make global changes to the URL patterns of your project while only touching a single file.
          - I guess it means we can do change our endpoints needless to change our codes.

# Views

-
