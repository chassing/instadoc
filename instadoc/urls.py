from __future__ import absolute_import

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

from main.api import v1_api


urlpatterns = patterns('',
  url(r'^api/', include(v1_api.urls)),
  url(r'^', include('%s.main.urls' % settings.PROJECT_NAME, namespace="main")),
)

if "django.contrib.admin" in settings.INSTALLED_APPS:
  urlpatterns += [url(r'^admin/', include(admin.site.urls))]
