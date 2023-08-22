from django.urls import path
from .views import (
    ReservationListView,
    ReservationDetailView,
    ReservationTimesView,
    ReservationCreateView,
    ReservationDeleteView,
    )
from . import views


urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation-list'),
    path('<int:pk>/', ReservationDetailView.as_view(), name='reservation-detail'),
    path('new/', ReservationCreateView.as_view(), name='reservation-create'),
    path(
        '<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation-delete'
    ),
    path('times/', ReservationTimesView.as_view(), name='reservation-times'),
    path('date/', views.date_form, name='reservation-date'),
]
