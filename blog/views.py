from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-details.html'


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



