from django.db import models
from CustomUsers.models import CustomUser

class CustomClass(models.Model):
    name = models.TextField(max_length=50)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='taught_classes')
    CATEGORIES = (
        ('other', 'Other'),
        ('cloth', 'Cloth'),
        ('laptop', 'Laptop'),
        ('mobile', 'Mobile'),
        ('electronic', 'Electronic'),
        ('furniture', 'Furniture')
    )
    category = models.CharField(max_length=20, choices=CATEGORIES, default='other')
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(CustomUser, blank=True, through='ClassMTMStudent')

class ClassMTMStudent(models.Model):
    custom_class = models.ForeignKey(CustomClass, on_delete=models.CASCADE, related_name='ps')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ps')
    is_Paid_for = models.BooleanField(default=False)