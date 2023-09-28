from django.shortcuts import render
from rest_framework.permissions import BasePermission
from CustomUsers.models import LogicUser
# Create your views here.

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.is_Teacher:
                return True
        return False

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user:
            if user.user_permissions.is_Student:
                return True
        return False
    
class IsLogin(BasePermission):
    def has_permission(self, request, view):
        user = LogicUser.get_user(request = request)
        if user is not None:
            return True
        return False