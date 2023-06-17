import os
import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
django.setup()

def create_staff_user(username, password):
    user = User.objects.create_user(username=username, password=password)
    user.is_staff = True
    user.save()

if __name__ == '__main__':
    create_staff_user('admin', 'password123')
