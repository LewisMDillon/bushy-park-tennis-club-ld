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
    path('contact', views.contact, name='website-contact'),
    path('base', views.base, name='website-base'),
    path('', views.home, name='website-home'),
    path('404', views.test_404, name='test-404'),
    path('403', views.test_403, name='test-403'),
    path('400', views.test_400, name='test-400'),
    path('500', views.test_500, name='test-500'),
]
