#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py migrate --noinput

# Auto-create superuser if it doesn't exist
# Auto-create or update superuser
python manage.py shell -c "
from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if User.objects.filter(username=username).exists():
    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()
    print('Superuser password updated')
else:
    User.objects.create_superuser(username=username, email=email, password=password)
    print('Superuser created')
"
python manage.py collectstatic --noinput