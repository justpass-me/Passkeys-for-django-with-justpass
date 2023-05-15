#!/bin/bash

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Apply database migrations"
python manage.py migrate

echo "Starting server"
echo `which python`
gunicorn -b 0.0.0.0:8000 Shop.wsgi:application --log-level=info