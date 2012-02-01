
from settings import *

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
