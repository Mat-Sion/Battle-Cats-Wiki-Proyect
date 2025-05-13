import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wiki.settings')
django.setup()

from django.core.management import call_command
call_command('makemigrations')
