from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSignupCustomUserSerializer
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsEditUser]

class CreateCustomUser(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginSignupCustomUserSerializer
    # permission_classes = [IsEditUser]

    def perform_create(self, serializer):
        serializer.save(password = make_password(self.request.data.get('password')))