DEBUG = True

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

MIDDLEWARE_CLASSES = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',

    'django_rq',

    'critical',
]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]

SITE_ID = 1
STATIC_URL = '/static/'

RQ_SHOW_ADMIN_LINK = True
RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'ASYNC': False,
    },
}

CRITICAL_CSS_ACTIVE = True
PENTHOUSE_HOST = 'localhost'
PENTHOUSE_CONFIG = {
    'width': '720',
    'propertiesToRemove': [
        '(.*)animation(.*)',
        '(.*)transition(.*)',
        '(.*)tap-highlight-color',
        '(.*)user-select',
        'cursor',
        'background-image',
        'pointer-events',
        'src',
        'will-change',
    ]
}
