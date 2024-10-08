from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


from .forms import LoginUserForm, RegisterUserForm


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_done')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register_done(request):
    return render(request, 'users/register_done.html')
