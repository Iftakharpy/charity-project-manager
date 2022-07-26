from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUserModel


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUserModel
    list_display = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "profile_picture",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
        "date_joined",
    )
    list_filter = (
        "is_staff",
        "is_active",
        "is_superuser",
        "email",
    )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Details", {"fields": ("first_name", "last_name", "phone_number", "profile_picture",)}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email", "password1", "password2"),
                "classes": ("wide",),
            },
        ),
        ("Details", {"fields": ("first_name", "last_name", "phone_number")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    search_fields = (
        "email",
        "first_name",
        "last_name",
        "phone_number",
    )
    ordering = (
        "email",
        "is_active",
        "is_superuser",
        "is_staff",
    )


admin.site.register(CustomUserModel, CustomUserAdmin)
