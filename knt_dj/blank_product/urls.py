from django.urls import path, include
from rest_framework import routers

from blank_product.views import BlankProductListView

router = routers.DefaultRouter()
router.register('', BlankProductListView)
urlpatterns = [
    path('', include(router.urls)),
]
