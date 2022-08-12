from django.http.request import HttpRequest
from rest_framework import serializers

from .models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserModel
        read_only_fields = ['password', 'is_active', 'is_staff', 'is_superuser',
                            'groups', 'user_permissions', 'date_joined', 'last_login']
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'profile_picture',

            'groups',
            'user_permissions',

            'is_active',
            'is_staff',
            'is_superuser',

            # 'password',
            'last_login',
            'date_joined',
        ]

    extra_kwargs = {
        'email': {
            'required': False
        },
        'phone_number': {
            'required': False
        },
    }
