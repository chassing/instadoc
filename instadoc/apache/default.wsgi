
import os
import sys
import site
os.environ["CELERY_LOADER"] = "django"

DJANGO_PROJECT_ROOT = "{{ code_root }}"
PROJECT_ROOT = os.path.dirname(DJANGO_PROJECT_ROOT)
# get environment name from wsgi file
ENV = os.path.basename(__file__).split(".")[0]

site_packages = os.path.join(PROJECT_ROOT, 'env/lib/python%d.%d/site-packages' % (sys.version_info[0], sys.version_info[1]))
site.addsitedir(os.path.abspath(site_packages))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, DJANGO_PROJECT_ROOT)
os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings_%s' % (os.path.basename(DJANGO_PROJECT_ROOT), ENV)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
