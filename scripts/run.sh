#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

celery -A app worker -l info

celery -A app flower --address=0.0.0.0

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi
