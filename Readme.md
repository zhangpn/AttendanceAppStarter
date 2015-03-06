To install django:
First, remove existing/outdated version by finding the path:
    run `python -c "import sys; sys.path = sys.path[1:]; import django; print(django.__path__)"`
    remove the django directory from the site-package or dist-package directory
`sudo apt-get install python3-pip`
`sudo pip3 install Django`

Run the following commands:
`django-admin.py startproject mysite`
`python3 manage.py migrate`
`python3 manage.py startapp attendance`
In `mysite1/settings.py` add `attendance` in the `INSTALLED_APPS` list
run `python3 manage.py createsuperuser` to create a new admin user
After modifying the models.py file, run `python3 manage.py makemigrations`, which can be skipped first
followed by `python3 manage.py migrate`
