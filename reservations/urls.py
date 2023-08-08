from django.urls import path
from .views import (
    ReservationListView,
    )
from . import views


urlpatterns = [
    path('reservation/', ReservationListView.as_view(), name='reservation'),
]
