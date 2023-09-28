from rest_framework import serializers
from .models import CustomClass
from CustomUsers.serializers import CustomUserSerializer

# class CustomClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = 
#         fields = ['id', 'name', 'teacher', 'category', 'description', 'date', 'students']

class CustomClassSerializer(serializers.ModelSerializer):
    teacher = CustomUserSerializer()
    class Meta:
        model = CustomClass
        fields = ['id', 'name', 'teacher', 'category', 'description', 'date', 'students']
