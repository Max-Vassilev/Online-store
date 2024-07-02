from django.contrib import admin
from .models import TechItem

@admin.register(TechItem)
class UserModelAdmin(admin.ModelAdmin):
    pass