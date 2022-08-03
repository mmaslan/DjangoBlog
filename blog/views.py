from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post
from django.views.generic import DetailView


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


