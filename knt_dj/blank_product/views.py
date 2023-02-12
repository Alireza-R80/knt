from django.shortcuts import render
from rest_framework import viewsets, status

from .permissions import DesignerGetOnly
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response


class BlankProductTypeViewSet(viewsets.ModelViewSet):
    queryset = BlankProductType.objects.all()
    serializer_class = BlankProductTypeSerializer
    permission_classes = (DesignerGetOnly,)
    # def retrieve(self, request, *args, **kwargs):
    #   response = {'You cant get prop separately from blank product'}
    #  return Response(response, status=status.HTTP_400_BAD_REQUEST)


class PropByBlankProductListView(generics.ListAPIView):
    serializer_class = BlankProductPropSerializer
    permission_classes = (DesignerGetOnly,)

    def get_queryset(self):
        return BlankProductProp.objects.filter(blank_product__id=self.kwargs['bpID'])


class BlankProductViewSet(viewsets.ModelViewSet):
    queryset = BlankProduct.objects.all()
    serializer_class = BlankProductSerializer
    permission_classes = (DesignerGetOnly,)


class BlankProductByCategoryListView(generics.ListAPIView):
    serializer_class = BlankProductSerializer
    permission_classes = (DesignerGetOnly,)

    def get_queryset(self):
        return BlankProduct.objects.filter(
            category__in=Category.objects.get(slug=self.kwargs['slug']).get_descendants(include_self=True))


class BlankProductByTypeListView(generics.ListAPIView):
    serializer_class = BlankProductSerializer
    permission_classes = (DesignerGetOnly,)

    def get_queryset(self):
        return BlankProduct.objects.filter(type__id=self.kwargs['typeID'])


class AvailableBlankProductListView(generics.ListAPIView):
    serializer_class = BlankProductSerializer
    permission_classes = (DesignerGetOnly,)

    def get_queryset(self):
        return BlankProduct.objects.filter(is_available=True)


class BlankProductPropValueViewSet(viewsets.ModelViewSet):
    queryset = BlankProductPropValue.objects.all()
    serializer_class = BlankProductPropValueSerializer
    permission_classes = (DesignerGetOnly,)


class BlankProductImageViewSet(viewsets.ModelViewSet):
    queryset = BlankProductImage.objects.all()
    serializer_class = BlankProductImageSerializer
    permission_classes = (DesignerGetOnly,)


class BlankProductSampleImageViewSet(viewsets.ModelViewSet):
    queryset = BlankProductSampleImage.objects.all()
    serializer_class = BlankProductSampleImageSerializer
    permission_classes = (DesignerGetOnly,)


class ProductProvidersPropViewSet(generics.ListAPIView):
    serializer_class = ProductProviderPropSerializer
    permission_classes = (DesignerGetOnly,)

    def get_queryset(self):
        return ProductProviderProp.objects.filter(blank_product__id=self.kwargs['bpiID'])


class ProductProviderPropViewSet(generics.RetrieveAPIView):
    serializer_class = ProductProviderPropSerializer
    permission_classes = (DesignerGetOnly,)

    def get_queryset(self):
        provider_id = self.request.data['providerID']
        return ProductProviderProp.objects.get(blank_product__id=self.kwargs['bpiID'], provider__id=provider_id)

# Create your views here.
