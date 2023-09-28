from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from CustomUserPermissions.models import CustomUserPermission
import jwt

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_permissions', CustomUserPermission.objects.create(Is_Teacher=True, Is_Student=True))
        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    user_permissions = models.OneToOneField(CustomUserPermission, on_delete=models.CASCADE, null=True, blank=True)
    #############################################################################
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #############################################################################
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.email

class LogicUser:
    def get_user(request):
        user = None
        try:
            username = request.user.username
            user = CustomUser.objects.get(username=username)
        except:
            pass
        return user