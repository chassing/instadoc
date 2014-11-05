
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL_WITH_RELATIONS

from instadoc.main.models import Documentation
from instadoc.main.models import Category


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        filtering = dict(
            id=("exact",),
        )


class DocumentationResource(ModelResource):
    category = fields.ForeignKey(CategoryResource, 'category')

    class Meta:
        queryset = Documentation.objects.all()
        list_allowed_methods = ['get']
        detail_allowed_methods = ['get']
        filtering = dict(
            category=ALL_WITH_RELATIONS,
            item=('icontains',),
            id=('exact',),
        )
