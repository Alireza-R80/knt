from rest_framework import serializers
from blank_product.models import *
from utils.serializers import SizeSerializer, ColorSerializer
from account.serializers import PrintProviderMiniSerializer


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'parent', 'is_active')


class CategoryMiniSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BlankProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductType
        fields = ('id', 'name', 'image', 'alt_text')


class BlankProductTypeMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductType
        fields = ('id', 'name')


class BlankProductPropSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductProp
        fields = ('id', 'name', 'type')


class BlankProductPropMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductProp
        fields = ('id', 'name')


class BlankProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductImage
        fields = ('id', 'blank_product', 'image', 'alt_text', 'is_preview')


class BlankProductSampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlankProductSampleImage
        fields = ('id', 'blank_product', 'sample_file')


class BlankProductPropValueSerializer(serializers.ModelSerializer):
    blank_prop = BlankProductPropMiniSerializer(read_only=True)

    class Meta:
        model = BlankProductPropValue
        fields = ('id', 'blank_product', 'blank_prop', 'value')


class BlankProductSerializer(serializers.ModelSerializer):
    category = CategoryMiniSerializers(read_only=True)
    type = BlankProductTypeMiniSerializer(read_only=True)
    blank_product_images = BlankProductImageSerializer(many=True)
    blank_product_sample_images = BlankProductSampleImageSerializer(many=True)
    blank_prop_values = BlankProductPropValueSerializer(many=True)

    class Meta:
        model = BlankProduct
        fields = ('id', 'title', 'category', 'type', 'description', 'is_available', 'blank_product_images',
                  'blank_product_sample_images', 'blank_prop_values', 'get_avg_price')


class ProductProviderDetailSerializer(serializers.ModelSerializer):
    color = ColorSerializer(read_only=True)
    size = SizeSerializer(read_only=True)

    class Meta:
        model = ProductProviderDetail
        fields = ('id', 'product_provider_prop', 'color', 'size')


class ProductProviderPropSerializer(serializers.ModelSerializer):
    ppd = ProductProviderDetailSerializer(many=True)
    provider = PrintProviderMiniSerializer(read_only=True)

    class Meta:
        model = ProductProviderProp
        fields = ('id', 'blank_product', 'provider', 'price', 'prep_time', 'ppd')
