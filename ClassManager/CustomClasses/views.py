from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from rest_framework.response import Response
from .models import CustomClass
from .serializers import CustomClassSerializer, CreateCustomClassSerializer
from CustomUsers.models import CustomUser
# Create your views here.
class CustomClassViewSet(viewsets.ModelViewSet):
    queryset = CustomClass.objects.all()
    serializer_class = CustomClassSerializer
    # permission_classes = [IsEditUser]

class CreateCustomClass(generics.CreateAPIView):
    queryset = CustomClass.objects.all()
    serializer_class = CreateCustomClassSerializer
    # permission_classes = [IsEditUser]

    def perform_create(self, serializer):
        email = self.request.user
        user = CustomUser.objects.get(email=email)
        if user is None:
            return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        serializer.save(teacher=user)

class ShowCustomClass(generics.RetrieveAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomClass.objects.all()
    serializer_class = CustomClassSerializer
    lookup_field = 'id'

class UpdateCustomClass(generics.UpdateAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomClass.objects.all()
    serializer_class = CreateCustomClassSerializer

    def perform_update(self, serializer):
        instance = serializer.instance
        email = self.request.user
        user = CustomUser.objects.get(email=email)
        teacher_data = instance.teacher
        if user != teacher_data:
            return Response({'error': 'User Not Allowed.'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

class DeleteCustomClass(generics.DestroyAPIView):
    # permission_classes = [IsEditUser]
    queryset = CustomClass.objects.all()
    serializer_class = CustomClassSerializer