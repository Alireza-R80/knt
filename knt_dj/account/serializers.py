from rest_framework import serializers

from account.models import BaseUser, Designer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('id', 'phone_number', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class DesignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designer
        fields = ('id', 'parent_user', 'card_number', 'balance', 'is_premium')
