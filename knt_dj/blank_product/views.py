from rest_framework import viewsets ,generics
from rest_framework.permissions import AllowAny

from blank_product.models import BlankProduct
from blank_product.serializers import BlankProductSerializer


class BlankProductListView(viewsets.ModelViewSet):
    queryset = BlankProduct.objects.all()
    serializer_class = BlankProductSerializer
    permission_classes = (AllowAny,)

