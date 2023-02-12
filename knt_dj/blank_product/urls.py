from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('type', BlankProductTypeViewSet)
router.register('prop_value', BlankProductPropValueViewSet)
router.register('image', BlankProductImageViewSet)
router.register('sample_image', BlankProductSampleImageViewSet)
router.register('', BlankProductViewSet)

urlpatterns = [
    path('prop/find_by_blank_product/<int:bpID>', PropByBlankProductListView.as_view(), name='blank_product_prop'),
    path('find_by_category/<slug:slug>', BlankProductByCategoryListView.as_view(), name='category_item'),
    path('find_by_type/<int:typeID>', BlankProductByTypeListView.as_view(), name='type_item'),
    path('available/', AvailableBlankProductListView.as_view(), name='available_blank_product'),
    path('product_provider/find_by_blank_product/<int:bpID>', ProductProvidersPropViewSet.as_view(),
         name='product_providers_prop'),
    path('product_provider/<int:bpID>', ProductProviderPropViewSet.as_view(),
         name='product_provider_prop'),
    path('', include(router.urls)),
]
