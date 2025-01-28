from django.contrib import admin
from .models import Profile

@admin.register(Profile)
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
