import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wiki.settings')
django.setup()

from django.contrib.auth.models import User

username = 'admin'
password = 'admin123'
email = 'admin@example.com'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superuser created successfully!')
    print(f'Username: {username}')
    print(f'Password: {password}')
else:
    print('Superuser already exists.')