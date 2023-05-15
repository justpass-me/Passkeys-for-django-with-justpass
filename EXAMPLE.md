# Use of Example project

**NOTE**: The example is configured to use the phone number to identify users so take care when create the 

1. create virtual env
`virtualenv env`
1. activate env `source env/bin/activate`
1. install requirements `pip install -r example/requirements.txt`
1. cd to example project `cd example`
1. migrate `python manage.py migrate`
1. create super user `python manage.py createsuperuser`
1. start the server `python manage.py runserver`
