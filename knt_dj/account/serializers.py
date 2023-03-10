from rest_framework import serializers

from account.models import BaseUser, Designer, PrintProviderAddress, PrintProvider
from utils.serializers import StateSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        read_only_fields = (
            'role', 'is_active'
        ),
        fields = ('id', 'phone_number', 'password', 'role', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class DesignerSerializer(serializers.ModelSerializer):
    parent_user = UserSerializer(read_only=True)

    class Meta:
        model = Designer
        fields = ('id', 'parent_user', 'card_number', 'balance', 'is_premium')


class PrintProviderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintProviderAddress
        fields = (
            'id', 'print_provider', 'state', 'city', 'detail', 'post_code', 'phone_number', 'is_default'
        )


class PrintProviderAddressMiniSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = PrintProviderAddress
        fields = ('id', 'state')


class PrintProviderSerializer(serializers.ModelSerializer):
    print_provider_address = PrintProviderAddressSerializer(many=False)
    parent_user = UserSerializer(read_only=True)

    class Meta:
        model = PrintProvider
        read_only_fields = (
            'rate'
        ),
        fields = (
            'id', 'parent_user', 'name', 'description', 'rate', 'print_provider_address',
        )


class PrintProviderMiniSerializer(serializers.ModelSerializer):
    print_provider_address = PrintProviderAddressMiniSerializer(many=False)

    class Meta:
        model = PrintProvider
        read_only_fields = (
            'rate'
        ),
        fields = (
            'id', 'name', 'rate', 'print_provider_address',
        )
