from django.shortcuts import render
from django.views.generic import ListView
from .models import Reservation


class ReservationListView(ListView):
    model = Reservation
    template_name = 'website/reservation.html'
    ordering = ['-date_created']
