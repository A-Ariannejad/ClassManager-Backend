from django.db import models
from CustomUsers.models import CustomUser

class CustomClass(models.Model):
    name = models.TextField(max_length=50)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    CATEGORIES = (
        ('other', 'Other'),
        ('cloth', 'Cloth'),
        ('laptop', 'Laptop'),
        ('mobile', 'Mobile'),
        ('electronic', 'Electronic'),
        ('furniture', 'furniture')
    )
    category = models.CharField(max_length=20, choices=CATEGORIES, default='other')
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)