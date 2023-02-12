from rest_framework import serializers

from account.models import Customer, Designer, PrintProviderAddress, PrintProvider


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
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


class PrintProviderSerializer(serializers.ModelSerializer):
    print_provider_addresses = PrintProviderAddressSerializer(many=False)

    class Meta:
        model = PrintProvider
        read_only_fields = (
            'role', 'is_active', 'rate'
        ),
        fields = (
            'id', 'phone_number', 'full_name', 'password', 'print_provider_addresses', 'role', 'is_active', 'rate'
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
