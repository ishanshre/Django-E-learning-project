from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from user.forms import CustomUserChangeForm, CustomUserCreationForm
from user.models import Profile
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    list_display = ['username','email','is_staff','email_verified']
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Extras", {
            "fields":("date_of_birth","email_verified",),
        }),
    )
    add_fieldsets = (
        (
            "Create User", {
                "classes":("wide",),
                "fields":("username","email","password1","password2"),
            }
        ),
    )
    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileInline]
        return []
