
from tastypie.api import NamespacedApi

from resources import DocumentationResource
from resources import CategoryResource


v1_api = NamespacedApi(api_name='v1')

v1_api.register(DocumentationResource())
v1_api.register(CategoryResource())
