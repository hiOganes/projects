from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Логин'}),
        )
    password = forms.CharField(
        max_length=255, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
        )


    class Meta:
        model = get_user_model()
        fields = ['username', 'password']