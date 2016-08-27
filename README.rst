=====
Lioncore
=====

Lioncore provides the core components for the Lionschool project. This package
is required for all other Lionschool packages.

Quick start
-----------

1. Add "lioncore" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Run `python manage.py migrate` to create the lioncore models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create users, teachers, grades, courses and more (you'll need the Admin
   app enabled).

5. Install other lionschool apps for more fun
