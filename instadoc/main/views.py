
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404


from models import Category


class Index(TemplateView):
  template_name = 'main/index.html'

  def get(self, request, pk=None):
    tmpl = RequestContext(request)
    tmpl["categories"] = Category.objects.all()
    tmpl["selected_category"] = get_object_or_404(Category, pk=1)
    if pk:
      tmpl["selected_category"] = get_object_or_404(Category, pk=pk)
    return self.render_to_response(tmpl)

