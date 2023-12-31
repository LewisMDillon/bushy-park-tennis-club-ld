from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )

from django.urls import reverse_lazy
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all(),
        'latest_post': Post.objects.last(),
        'second_last_post': Post.objects.filter().order_by('-pk')[1],
        'third_last_post': Post.objects.filter().order_by('-pk')[2],
    }
    return render(request, 'website/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'website/news.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "The post was created successfully")
        return super().form_valid(form)

    def test_func(self):
        if self.request.user.is_staff:
            return True
        elif self.request.user.is_superuser:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content', 'image']

    def form_valid(self, form):
        messages.success(self.request, "The post was updated successfully")
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        elif self.request.user.is_superuser:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('website-news')
    success_message = (
        'The post was deleted successfully'
    )

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        elif self.request.user.is_superuser:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    return render(request, 'website/contact.html')


def base(request):
    return render(request, 'website/base.html')
