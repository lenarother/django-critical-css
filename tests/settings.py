DEBUG = True

SECRET_KEY = 'test'

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}

MIDDLEWARE_CLASSES = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django_rq',
    'inline_static',
    'critical',
]

TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates', 'APP_DIRS': True}]

SITE_ID = 1
STATIC_URL = '/static/'

RQ_SHOW_ADMIN_LINK = True
RQ_QUEUES = {'default': {'HOST': 'localhost', 'PORT': 6379, 'DB': 0, 'ASYNC': False}}

CRITICAL_CSS_ACTIVE = True
PENTHOUSE_URL = 'http://localhost:3000/'
CRITICAL_CSS_IGNORE_QUERY_STRING = False

try:
    import cms  # noqa

    GLOBAL_INSTALLED_APPS = INSTALLED_APPS
    from .cms_settings import *  # noqa

    INSTALLED_APPS = GLOBAL_INSTALLED_APPS + INSTALLED_APPS
except ImportError:
    pass
