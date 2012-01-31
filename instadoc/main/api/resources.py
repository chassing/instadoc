
from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.constants import ALL_WITH_RELATIONS

from ..models import Documentation
from ..models import Category


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
    #excludes = ['html']
    filtering = dict(
      category=ALL_WITH_RELATIONS,
      item=('icontains',),
    )

  def get_list(self, request, **kwargs):
    """ patched tastypie 'get_list' method. removes html attribute from all objects in list view
    """
    objects = self.obj_get_list(request=request, **self.remove_api_resource_names(kwargs))
    sorted_objects = self.apply_sorting(objects, options=request.GET)

    paginator = self._meta.paginator_class(request.GET, sorted_objects, resource_uri=self.get_resource_list_uri(), limit=self._meta.limit)
    to_be_serialized = paginator.page()

    # Dehydrate the bundles in preparation for serialization.
    bundles = [self.build_bundle(obj=obj, request=request) for obj in to_be_serialized['objects']]
    to_be_serialized['objects'] = [self.full_dehydrate(bundle) for bundle in bundles]
    for obj in to_be_serialized['objects']:
      del obj.data['html']
    to_be_serialized = self.alter_list_data_to_serialize(request, to_be_serialized)
    return self.create_response(request, to_be_serialized)

