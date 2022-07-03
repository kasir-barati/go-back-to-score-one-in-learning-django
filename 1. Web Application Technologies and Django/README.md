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
        - `makemigrations`:
          - Creates new migrations based on the changes detected to your models.
          - Watch our current `models.py` and see if there is any change. If there was it will create a new migration
          - **You can remove the generated migration files. Just remember that do not remove applied migration. Since Django keep track of applied migrations on the database as we have the same behavior in Prisma. But in dev env you can remove the migration file and database too.**
        - `migrate`:
          - To apply created migrations to database
        - sendtestemail
        - `shell`
          - `python manage.py shell`
          - Auto bind your projects' packages into a interactive Python
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

# MVC in Django

- `urls.py` are kinda our controllers
- `views.py` are view and controller
- `models.py` are models

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

# Models

- [Django official doc](https://docs.djangoproject.com/en/4.0/topics/db/queries/)
- [Related lecture link](https://www.dj4e.com/lectures/DJ-02-Model-Single.txt)
- Each model has one [`Manager`](https://docs.djangoproject.com/en/4.0/topics/db/managers/#django.db.models.Manager), and it’s called `objects` by default.
  - Access it directly via the model class, like so:
    - `User.objects`
- An intuitive system to represent database-table data in Python objects
  - Extends/Inheritance from `Model` which is in the `django.db.models`
  - Define field types in `modes.py`
  - A model class represents a database table
    - An instance of class represents a particular record
- `filter` create the `where` clause for us
- We have ORM in place. You do not need to install ORM
  - Abstract layer on top SQL database management systems
  - But why ORM?
    - Just python not SQL
    - More readily change your database
    - A powerful built-in migration system
    - Automatic form generation and validation
- How many query executed against database:
  ```py
  q = Article.objects.filter(headline__startswith="What")
  q = q.filter(pub_date__lte=datetime.date.today())
  q = q.exclude(body_text__icontains="food")
  print(q)
  ```
  - Though **this looks like three database hits**, in fact **it hits the database only once**, at the last line (`print(q)`). In general, the results of a `QuerySet` ain't fetched from the database until you "ask" for them. When you use the `QuerySet` it is evaluated by accessing the database.
- **CRUD**
  - Create:
    - `u = User(name='Kristen', email='kf@umich.edu')`
      - It is not saved in db, yet. `u.save()`
        - `.save` has no return value.
      - You can alternatively use `User.create()` to create and save the new record at once.
  - Read:
    - A list of options:
      - contains
      - icontains
      - startswith
      - endswith
      - iendswith
      - istartswith
    - Automatic join:
      ```py
      class Blog(models.Model):
          name = models.CharField(max_length=100)
          tagline = models.TextField()
          def __str__(self):
              return self.name
      class Entry(models.Model):
          blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
          headline = models.CharField(max_length=255)
          body_text = models.TextField()
          pub_date = models.DateField()
          mod_date = models.DateField(default=date.today)
          authors = models.ManyToManyField(Author)
          number_of_comments = models.IntegerField(default=0)
          number_of_pingbacks = models.IntegerField(default=0)
          rating = models.IntegerField(default=5)
          def __str__(self):
              return self.headline
      Entry.objects.filter(blog__name='Beatles Blog')
      ```
    - JSON fields:
      ```py
      class Dog(models.Model):
          name = models.CharField(max_length=200)
          data = models.JSONField(null=True)
          def __str__(self):
              return self.name
      Dog.objects.create(name='Rufus', data={
          'breed': 'labrador',
          'owner': {
              'name': 'Bob',
              'other_pets': [{
                  'name': 'Fishy',
              }],
          },
      })
      Dog.objects.filter(data__owner__name='Bob')
      ```
    - These queries return an `QuerySet`
      - A `QuerySet` represents a collection of objects from database.
      - `QuerySet` equates to a `SELECT` statement
      - Each `QuerySet` contains a cache to minimize database access.
    - `User.objects.values()`
    - `User.objects.values().order_by('-name')`
    - `User.objects.filter(email='csev@umich.edu').values()`
      - Add a `WHERE` clause to return a narrow result.
        - **Caution**
          ```py
          Blog.objects.exclude(
              entry__headline__contains='Lennon',
              entry__pub_date__year=2008,
          )
          ```
          This query would exclude blogs that contain "Lennon" in the headline or published in 2008. If you need that you should perform 2 query:
          ```py
          Blog.objects.exclude(
              entry__in=Entry.objects.filter(
                  headline__contains='Lennon',
                  pub_date__year=2008,
              ),
          )
          ```
        - Compare the value of a model field with another field on the same model:
          - `F expressions`
          - Author’s name is the same as the blog name
            ```py
            from django.db.models import F
            Entry.objects.filter(authors__name=F('blog__name'))
            ```
    - Get by ID:
      ```py
      Blog.objects.get(id__exact=14) # Explicit form
      Blog.objects.get(id=14) # __exact is implied
      Blog.objects.get(pk=14) # pk implies id__exact
      Blog.objects.filter(pk__in=[1,4,7]) # With id 1, 4 and 7
      Blog.objects.filter(pk__gt=14) # id > 14
      ```
    - `Article.objects.filter(headline__startswith="What")`
      - Pass an invalid keyword argument, it will raise `TypeError`.
      - If there should be only one object that matches your query use `get()`
        - `User.objects.get(pk=1)`
        - "exact" and "iexact" match:
          - iexact is just case-insensitive
          - `Blog.objects.get(slug__exact='some-blog') # Explicit form`
          - `Blog.objects.get(slug='some-blog') # __exact is implied`
            - `WHERE id = 'some-blog'`
        - It will raise:
          - `DoesNotExist` exception if there was no record
          - `MultipleObjectsReturned` exception if there were more than one record
    - `LIMIT` and `OFFSET` clauses.
      - `User.objects.all()[:5]` LIMIT = 5
      - `User.objects.all()[5:10]` OFFSET = 5, and LIMIT = 5
  - Update:
    - `User.objects.filter(email='csev@umich.edu').update(name='Charles')`
      - `filter` is a limiting clause such as `WHERE` or `LIMIT`.
      - Returns a new `QuerySet` containing objects that match the given lookup parameters.
      - Always give you a `QuerySet`
  - Delete:
    - `delete()`
      - Deletes the object and returns the number of objects deleted and a dictionary with the number of deletions per object type.
    - `User.objects.exclude(email='ted@umich.edu').delete()`
      - Returns a new `QuerySet` containing objects that do not match the given lookup parameters. and delete them
    - It does SQL constraint `ON DELETE CASCADE`
      - Customizable via the `on_delete` argument to the `ForeignKey`.
