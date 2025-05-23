from django.contrib import admin

from .models import User


@admin.register(User)
class Users(admin.ModelAdmin):
    list_display = ("email", "username",)
    search_fields = ("email__startswith", "username__startswith")

