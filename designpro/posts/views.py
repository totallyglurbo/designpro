from django.shortcuts import render
from django.views import generic

from .models import Post


def index(request):
    posts = Post.objects.all()[:4]
    context = {'posts': posts}
    return render(request, 'index.html', context)


