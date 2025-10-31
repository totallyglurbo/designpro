from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
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
        form = RegistrationForm(request.POST)
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'profile.html')


def logout_view(request):
    logout(request)
    return redirect('/')


