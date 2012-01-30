
from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

APP_ROOT_URL = ""
MEDIA_URL = '%s/media/' % APP_ROOT_URL
STATIC_URL = '%s/static' % APP_ROOT_URL
ADMIN_MEDIA_PREFIX = '%s/static/admin/' % APP_ROOT_URL
LOGIN_URL = "%s/login/" % APP_ROOT_URL
LOGOUT_URL = "%s/logout/" % APP_ROOT_URL
LOGIN_REDIRECT_URL = "%s/" % APP_ROOT_URL

PUBLIC_VERSION = True

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': '%s' % PROJECT_NAME.lower(),
    'USER': '%s' % PROJECT_NAME.lower(),
    'PASSWORD': 'foobar',
    'HOST': '127.0.0.1',
    'PORT': '',
  },
}


import logging
logging.getLogger().setLevel(logging.INFO)

LOGGING["loggers"]["main"] = {
  'handlers': ['logfile'],
  'level': 'INFO',
}

# remove unneeded apps
INSTALLED_APPS.remove("django_nose")
INSTALLED_APPS.remove("django.contrib.admin")
