from .base import *
from . import db


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["net.jc-django.tk", "www.jc-django.tk", "jc-django.tk", "129.151.110.171"]


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = db.SQLITE3


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR.child('static'),
]
STATIC_ROOT = BASE_DIR.child('staticfiles')


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR.child('media')
