# -*- coding: utf-8 -*-

import os

DIRNAME = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dndtools',
        'USER': 'dndtools',
        'PASSWORD': 'dndtools',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
            },
        }
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'dndtools'

MEDIA_ROOT = os.path.join(DIRNAME, 'static/')

SITE_ID = 1

INTERNAL_IPS = ('127.0.0.1', )

TEMPLATE_DIRS = (
     os.path.join(DIRNAME, 'templates/'),
)
RECAPTCHA_PUBLIC = 'TODO FILL'
RECAPTCHA_PRIVATE = 'TODO FILL'
