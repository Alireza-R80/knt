from rest_framework import serializers
from .models import *


class ProductRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRate
        fields = ('id', 'user', 'rate')


class ProductReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReport
        fields = ('id', 'user', 'product', 'status')


class ProductCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComment
        fields = ('id', 'user', 'title')
