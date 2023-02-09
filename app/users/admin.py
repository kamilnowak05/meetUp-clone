from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ("id",)
    list_display = ("email", "is_staff", "admin", "photo")
    search_fields = ("email", "is_staff", "admin")
    list_filter = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name", "interests", "photo")}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "admin")}),
        (_("Important date"), {"fields": ("last_login",)}),
    )
    add_fieldsets = ((None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),)


admin.site.register(User, UserAdmin)
