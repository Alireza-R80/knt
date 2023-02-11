from rest_framework import serializers
from .models import *


class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'code')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ('id', 'unit')


