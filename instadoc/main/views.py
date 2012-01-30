
from django.template import RequestContext
#from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


class Index(TemplateView):
  template_name = 'main/index.html'

  def get(self, request):
    tmpl = RequestContext(request)
    return self.render_to_response(tmpl)

