# Django Blog
<p align="center">
  <span>English</span> |
  <a href="https://github.com/Fonsii/blog-django-mongodb/blob/main/lang/spanish/README.md">Español</a>
</p>


This is a simple blog build in django using MongoDB as database

<p align="center" width="100%">
    <img width="33%" src="https://github.com/Fonsii/blog-django-mongodb/blob/main/resources/readme_utils/web_blog_main_page.png"> 
</p>

Clone the repository

    git clone [paste link to this]

Open the file

    cd blog-django-mongodb

Now, use virtual venv for dependencies

    pip install django
    pip install djongo
    pip install Pillow

Before you run the server, have to change settings databases and run

    py manage.py makemigrations
    py manage.py migrate

The you can run the code and have fun!

    py manage.py runserver
    
Or

    python manage.py runserver

**This project uses English**