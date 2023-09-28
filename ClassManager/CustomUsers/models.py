from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from CustomUserPermissions.models import CustomUserPermission
from CustomClasses.models import CustomClass, ClassMTMStudent
import jwt

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Username field must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('user_permissions', CustomUserPermission.objects.create(Is_Teacher=True, Is_Student=True))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True, max_length=50)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    user_permissions = models.OneToOneField(CustomUserPermission, on_delete=models.CASCADE, null=True, blank=True)
    custom_classes = models.ManyToManyField(CustomClass, blank=True, through=ClassMTMStudent)
    #############################################################################
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    #############################################################################
    objects = UserManager()

    USERNAME_FIELD = 'email'
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
            email = request.user.email
            user = CustomUser.objects.get(email=email)
        except:
            pass
        return user