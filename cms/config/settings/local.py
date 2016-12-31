from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cms',
        'USER': 'cmsuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}