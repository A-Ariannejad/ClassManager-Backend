from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSignupCustomUserSerializer, UpdateCustomUserSerializer
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


class MyCustomUser(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    # permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        try:
            user_id = request.user.id
            user = CustomUser.objects.get(id=user_id)
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        
class ShowCustomUser(generics.RetrieveAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'

class UpdateCustomUser(generics.UpdateAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomUser.objects.all()
    serializer_class = UpdateCustomUserSerializer

    def perform_update(self, serializer):
        instance = serializer.instance
        email = self.request.user
        user = CustomUser.objects.get(email=email)
        if user != instance:
            print(instance , user)
            return Response({'error': 'User Not Allowed.'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()


class DeleteCustomUser(generics.DestroyAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_destroy(self, instance):
        email = self.request.user
        user = CustomUser.objects.get(email=email)
        if user != instance:
            return Response({'error': 'User Not Allowed.'}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()