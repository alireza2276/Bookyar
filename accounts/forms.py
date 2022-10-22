from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms
from .models import CustomUser

class CustomUserCreationForms(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', ]


class CustomUserChangeForms(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', ]