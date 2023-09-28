from rest_framework import serializers
from .models import CustomClass
from CustomUsers.models import CustomUser

# class CustomClassSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = 
#         fields = ['id', 'name', 'teacher', 'category', 'description', 'date', 'students']

class CreateCustomClassSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=True, required=True)
    class Meta:
        model = CustomClass
        fields = ['id', 'name', 'price', 'category', 'description', 'date', 'students']

class CustomClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomClass
        fields = '__all__'