from rest_framework import serializers

from account.models import BaseUser, Designer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        read_only_fields = (
            'role'
        ),
        fields = ('id', 'phone_number', 'password', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class DesignerSerializer(serializers.ModelSerializer):
    parent_user = UserSerializer(read_only=True)

    class Meta:
        model = Designer
        fields = ('id', 'parent_user', 'card_number', 'balance', 'is_premium')
