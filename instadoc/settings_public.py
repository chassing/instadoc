
from settings import *

try:
  from local_settings import *
except ImportError:
  pass

DEBUG = False
TEMPLATE_DEBUG = DEBUG

import logging
logging.getLogger().setLevel(logging.INFO)

LOGGING["loggers"]["main"] = {
  'handlers': ['logfile'],
  'level': 'INFO',
}

# remove unneeded apps
INSTALLED_APPS.remove("django_nose")
INSTALLED_APPS.remove("django.contrib.admin")


# sentry setup
if "SENTRY_CREDENTIALS" in locals():
  INSTALLED_APPS.append("raven.contrib.django")

  MIDDLEWARE_CLASSES += [
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
  ]

  SENTRY_DSN = SENTRY_CREDENTIALS

  LOGGING['root'] = {
    'level': 'WARNING',
    'handlers': ['sentry'],
  },
  LOGGING["handlers"]['sentry'] = {
    'level': 'ERROR',
    'class': 'raven.contrib.django.handlers.SentryHandler',
  }
  LOGGING["loggers"]['raven'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
  }
  LOGGING["loggers"]['sentry.errors'] = {
    'level': 'DEBUG',
    'handlers': ['console'],
    'propagate': False,
  }
