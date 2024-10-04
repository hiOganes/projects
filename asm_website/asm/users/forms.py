from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'container'}),
        label='Логин'
        )
    password = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'container'}),
        label='Пароль'
        )


    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'container'}),
        label='Логин'
        )
    password1 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'container'}),
        label='Пароль'
        )
    password2 = forms.CharField(
        max_length=255,
        widget=forms.PasswordInput(attrs={'class': 'container'}),
        label='Повторите пароль'
        )


    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']