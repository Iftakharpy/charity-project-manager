from rest_framework.serializers import ModelSerializer

from .models import CustomUserModel


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUserModel
        # exclude = ['password']
        read_only_fields = ['password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',]
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',

            'groups',
            'user_permissions',
            
            'is_active',
            'is_staff',
            'is_superuser',
            
            # 'password',
            'last_login',
            'date_joined',
            ]
