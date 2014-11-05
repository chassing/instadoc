
from django.template import RequestContext
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
