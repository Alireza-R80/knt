from rest_framework import serializers
from blank_product.models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'slug', 'parent', 'is_active')


class BlankProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductType
        fields = ('id', 'name', 'image', 'alt_text')


class BlankProductPropSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductProp
        fields = ('id', 'name', 'type')


class BlankProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductImage
        fields = ('id', 'blank_product', 'image', 'alt_text', 'is_preview')


class BlankProductSampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductSampleImage
        fields = ('id', 'blank_product', 'src')


class BlankProductPropValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductPropValue
        fields = ('id', 'blank_product', 'blank_prop', 'value')


class BlankProductSerializer(serializers.ModelSerializer):
    blank_product_images = BlankProductImageSerializer(many=True)
    blank_product_sample_images = BlankProductSampleImageSerializer(many=True)
    blank_prop_values = BlankProductPropValueSerializer(many=True)

    class Meta:
        model = BlankProduct
        fields = ('id', 'title', 'category', 'type', 'description', 'is_available', 'blank_product_images',
                  'blank_product_sample_images', 'blank_prop_values')
