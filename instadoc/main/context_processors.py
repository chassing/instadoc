
from django.conf import settings

def django_conf(request):
  return dict(
    APP_NAME=settings.APP_NAME,
    APP_VERSION=settings.APP_VERSION
  )

