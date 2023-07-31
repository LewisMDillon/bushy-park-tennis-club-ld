from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'website/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'website/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    return render(request, 'website/about.html')
