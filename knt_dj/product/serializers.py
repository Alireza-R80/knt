from rest_framework import serializers
from product.models import *


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'code')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'type', 'unit')


class ProductProviderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProviderDetail
        fields = ('id', 'product_provider_prop', 'color', 'size', 'price')


class ProductProviderPropSerializer(serializers.ModelSerializer):
    ppd = ProductProviderDetailSerializer(many=True)

    class Meta:
        model = ProductProviderProp
        fields = ('id', 'blank_product', 'provider', 'prep_time', 'ppd', 'get_min_price')
