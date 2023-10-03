from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class ContactAdmin(admin.ModelAdmin):
    pass