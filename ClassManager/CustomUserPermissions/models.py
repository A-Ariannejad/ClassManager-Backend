from django.db import models

class CustomUserPermission(models.Model):
    is_Teacher = models.BooleanField(default=False)
    is_Student = models.BooleanField(default=False)