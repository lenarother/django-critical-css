import os


LANGUAGE_CODE = 'de'

ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = [
    'cms',
    'treebeard',
    'menus',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
)

CMS_TEMPLATES = (('empty_template.html', 'empty'),)
CMS_TOOLBARS = [
    'cms.cms_toolbars.PlaceholderToolbar',
    'cms.cms_toolbars.BasicToolbar',
    'cms.cms_toolbars.PageToolbar',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'resources', 'templates')],
        'OPTIONS': {
            'debug': False,
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ],
        },
    },
]
