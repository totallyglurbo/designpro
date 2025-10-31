from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Post, ReallyUser
from .forms import RegistrationForm


def index(request):
    posts = Post.objects.all()[:4]
    context = {'posts': posts}
    return render(request, 'index.html', context)


class TheLoginView(LoginView):
    template_name = 'login.html'


class TheRegisterView(CreateView):
    model = ReallyUser
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'register.html'

@login_required
def profile_view(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('/')


