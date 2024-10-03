from django.shortcuts import render
from django.contrib.auth.views import LoginView

from .forms import LoginUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
