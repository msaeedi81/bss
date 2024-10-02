import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bss.settings')
application = get_wsgi_application()


from score_handler.models import Content
from django.contrib.auth.models import User


def create_content():
    Content.objects.create(title='Test Content 1', body='This is a test content.')
    Content.objects.create(title='Test Content 2', body='This is another test content.')
    Content.objects.create(title='Test Content 3', body='More test content.')


def create_user():
    User.objects.create_user(username='user1', password='password123')
    User.objects.create_user(username='user2', password='password123')
    User.objects.create_user(username='user3', password='password123')


def main():
    create_user()
    create_content()


if __name__ == '__main__':
    main()
