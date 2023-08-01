from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
    )
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='website-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about', views.about, name='website-about')
]
