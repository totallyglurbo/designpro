from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Post
from .forms import RegistrationForm


def index(request):
    posts = Post.objects.all()[:4]
    context = {'posts': posts}
    return render(request, 'index.html', context)


class TheLoginView(LoginView):
    template_name = 'login.html'


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
            return render(request, 'register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'category', 'description', 'post_image']
    template_name = 'post_form.html'
    success_url = reverse_lazy('index')

@login_required
def profile_view(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('/')
##




