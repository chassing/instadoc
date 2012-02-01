# Django settings

import os
import sys
DIRPATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_NAME = os.path.basename(DIRPATH)
sys.path.append("%s/site-packages" % DIRPATH)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
  ('Chris', 'chris@ca-net.org'),
)

MANAGERS = ADMINS

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': '%s/../db/db.sqlite' % DIRPATH,
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
    'OPTIONS': {
      'timeout': 5,
    }
  }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '%s/media/' % DIRPATH

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '%s/static/' % DIRPATH

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
  # Put strings here, like "/home/html/static" or "C:/www/django/static".
  # Always use forward slashes, even on Windows.
  # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
  'django.contrib.staticfiles.finders.FileSystemFinder',
  'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'adfadfa_n2e0tw#-iin92%ne9p@+_8n&ic+jfjzv&gynymo%p5-1!_-v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
  'django.template.loaders.filesystem.Loader',
  'django.template.loaders.app_directories.Loader',
  'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = [
  "django.contrib.auth.context_processors.auth",
  "django.core.context_processors.debug",
  "django.core.context_processors.i18n",
  "django.core.context_processors.media",
  "django.core.context_processors.static",
  "django.contrib.messages.context_processors.messages",
  "%s.main.context_processors.django_conf" % PROJECT_NAME
]

MIDDLEWARE_CLASSES = [
  'django.middleware.common.CommonMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = '%s.urls' % PROJECT_NAME

TEMPLATE_DIRS = [
  '%s/templates' % DIRPATH,
]

INSTALLED_APPS = [
  # std django apps
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.staticfiles',
  'django.contrib.admin',

  # restful api framework
  'tastypie',

  # db migrations
  'south',

  # django nose
  'django_nose',

  # my apps
  'main',
]

AUTHENTICATION_BACKENDS = [
  "django.contrib.auth.backends.ModelBackend",
]

LANGUAGES = (
  ('en', u'English'),
  #('de', u'Deutsch'),
)

import logging
logging.getLogger().setLevel(logging.DEBUG)


LOGGING = {
  'version': 1,
  'disable_existing_loggers': True,
  'formatters': {
    'std': {
      'format': '[%(asctime)s: %(levelname)s - %(name)s] %(message)s',
    }
  },
  'filters': {
  },
  'handlers': {
    'mail_admins': {
      'level': 'ERROR',
      'class': 'django.utils.log.AdminEmailHandler'
    },
    'console': {
      'class': 'logging.StreamHandler',
      'formatter': 'std',
    },
    'logfile': {
      'class': 'logging.handlers.RotatingFileHandler',
      'formatter': 'std',
      'filename': '%s/../log/%s.log' % (DIRPATH, PROJECT_NAME),
      'maxBytes': 1024 * 1024 * 2,
      'backupCount': 20,
    },
  },
  'loggers': {
    'django.request': {
      'handlers': ['mail_admins'],
      'level': 'ERROR',
      'propagate': False,
    },
    'django.request.tastypie': {
      'handlers': ['console'],
      'level': 'DEBUG',
    },
    'main': {
      'handlers': ['console'],
      'level': 'DEBUG',
    },
  }
}

#
# app settings
#
APP_NAME = "Instadoc"
APP_NAME_LONG = "Insta Doc"
APP_VERSION = "0.1"
COPYRIGHT_YEAR = "2012"


if 'tastypie' in INSTALLED_APPS:
  API_LIMIT_PER_PAGE = 0
  TASTYPIE_FULL_DEBUG = False

if 'django_nose' in INSTALLED_APPS:
  # bamboo test stuff
  TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
  NOSE_ARGS = [
    '--with-nosexunit',
  ]

