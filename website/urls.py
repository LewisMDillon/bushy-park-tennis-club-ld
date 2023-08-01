from django.urls import path
from .views import PostListView, PostDetailView
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='website-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about', views.about, name='website-about')
]
