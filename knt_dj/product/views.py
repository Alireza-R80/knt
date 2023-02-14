from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .permissions import GetOnly
from .serializers import *
from blank_product.models import ProductProviderProp, ProductProviderDetail


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (GetOnly,)

    def perform_create(self, serializer):
        colors = self.request.data.get('colors', False)
        if colors:
            product = serializer.save(designer=self.request.user)
            ProductImage.objects.create(product=product, image=product.design_img, alt_text=product.name, is_preview=True)
            pp = ProductProviderProp.objects.get(blank_product=product.blank_product, provider=product.provider)
            id = pp.id
            for color in colors:
                obj = ProductDetail.objects.create(product=product, color=color)
                for ppd in ProductProviderDetail.objects.filter(id=id, color__id=color):
                    obj.size.add(ppd.size)
                    obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(data='Color can not be empty', status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
