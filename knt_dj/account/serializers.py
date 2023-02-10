from rest_framework import serializers

from account.models import BaseUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = ('id','phone_number','password')
        extra_kwargs = {
            'password': {'write_only': True}
        }