from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from accounts.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['username', 'email', ]


