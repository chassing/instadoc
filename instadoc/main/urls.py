from django.conf.urls.defaults import patterns, url
from main.views import Index


urlpatterns = patterns('ta.main',
  url(r'^$', Index.as_view(), name="index"),
  url(r'^category/(?P<pk>.*)/$', Index.as_view(), name="category"),
)
