from rest_framework import serializers
from .models import CustomUserPermission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserPermission
        fields = ['id', 'is_Teacher', 'is_Student']
        