from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom Admin Model """

    CUSTOM_PROFILE = (
        "Custom Profile",
        {
            "fields": (
                "avatar",
                "gender",
                "bio",
                "birthdate",
                "language",
                "currency",
                "superhost",
            )
        },
    )
    # CUSTOM_USE = ("Customer Use", {"fields": ("language", "currency", "superhost",)})
    fieldsets = UserAdmin.fieldsets + (CUSTOM_PROFILE,)
    # fieldsets = UserAdmin.fieldsets + (CUSTOM_PROFILE, CUSTOM_USE)
    # I'll seperate in fields profile and sub options
