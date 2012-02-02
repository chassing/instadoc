
import logging
log = logging.getLogger("main.views")


from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404


from models import Category


class Index(TemplateView):
  template_name = 'main/index.html'

  def get(self, request, category=None):
    tmpl = RequestContext(request)
    tmpl["categories"] = Category.objects.all()
    tmpl["selected_category"] = get_object_or_404(Category, item='python')
    if category:
      tmpl["selected_category"] = get_object_or_404(Category, item=category.lower())
    return self.render_to_response(tmpl)

