from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    )
from . import views


urlpatterns = [
    path('news', PostListView.as_view(), name='website-news'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path(
        'post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'
        ),
    path(
        'post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'
        ),
    path('about', views.about, name='website-about'),
    path('index', views.index, name='website-index'),
    path('base', views.base, name='website-base'),
    path('', views.home, name='website-home'),
    path('', views.home, name='website-home'),
]
