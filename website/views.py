from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'Lewis',
#         'title': 'Blog Post 1',
#         'content': 'This is the first post',
#         'date_posted': '26th July, 2023'
#     },
#     {
#         'author': 'Lewis',
#         'title': 'Blog Post 2',
#         'content': 'This is the second post',
#         'date_posted': '27th July, 2023'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'website/home.html', context)


def about(request):
    return render(request, 'website/about.html')