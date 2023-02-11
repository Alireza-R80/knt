from rest_framework import serializers
from product.models import *


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = (
            'id', 'product', 'image', 'alt_text', 'is_preview'
        )


class ProductTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductTag
        fields = (
            'id', 'product', 'name'
        )


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDetail
        fields = (
            'id', 'product', 'color', 'size'
        )


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True)
    tags = ProductTagSerializer(many=True)
    product_details = ProductDetailSerializer(many=True)

    class Meta:
        model = BlankProduct
        read_only_fields = (
            'designer',
            'created_at',
            'modified_at',
            'status',
            'is_available'
        ),
        fields = ('id', 'name', 'description', 'blank_product', 'provider', 'design_img', 'sample_img', 'price',
                  'discount_percent', 'rate', 'images', 'tags', 'product_detail')
