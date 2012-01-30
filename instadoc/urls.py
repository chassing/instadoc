from __future__ import absolute_import

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

from main.api import v1_api


urlpatterns = patterns('',
  # main redirect
  url(r'^$', RedirectView.as_view(url="%s/main/" % settings.APP_ROOT_URL)),

  # main app
  url(r'^main/', include('%s.main.urls' % settings.PROJECT_NAME, namespace="main")),
  url(r'^api/', include(v1_api.urls)),


)

if "django.contrib.admin" in settings.INSTALLED_APPS:
  urlpatterns += [url(r'^admin/', include(admin.site.urls))]
