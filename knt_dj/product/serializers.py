from rest_framework import serializers

from blank_product.models import ProductProviderDetail, ProductProviderProp
from product.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'designer', 'status')


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'code')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'type', 'unit')


class ProductDetailSerializer(serializers.ModelSerializer):
    prd = ProductSerializer(many=True)
    product_color = ColorSerializers(many=True)
    product_size = SizeSerializer(many=True)

    class Meta:
        model = ProductDetail
        fields = ('id', 'prd', 'price', 'product_color', 'product_size')


class ProductProviderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProviderDetail
        fields = ('id', 'product_provider_prop', 'color', 'size', 'price')


class ProductProviderPropSerializer(serializers.ModelSerializer):
    ppd = ProductProviderDetailSerializer(many=True)

    class Meta:
        model = ProductProviderProp
        fields = ('id', 'blank_product', 'provider', 'prep_time', 'ppd', 'get_min_price')
