import random
from django.shortcuts import render

# Create your views here.
from posts.models import Post



def index(request,):
    posts = Post.objects.all()
    return render(request, 'layout.html', {'posts': posts})

