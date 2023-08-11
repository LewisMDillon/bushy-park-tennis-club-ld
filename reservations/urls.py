from django.urls import path
from .views import (
    ReservationListView,
    ReservationTimesView,
    ReservationCreateView,
    )
from . import views


urlpatterns = [
    path('', ReservationListView.as_view(), name='reservation-list'),
    path('new/', ReservationCreateView.as_view(), name='reservation-create'),
    path('times/', ReservationTimesView.as_view(), name='reservation-times'),
]
