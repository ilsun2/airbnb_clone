from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    
    fieldsets = UserAdmin.fieldsets + (
        ("custom",{"fields":(
            "bio",
"avatar",
"birthday",
"gander"
        )}),
    )