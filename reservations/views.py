from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from .models import Reservation
import datetime


class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservations/reservation_list.html'
    context_object_name = 'reservations'
    ordering = ['-date_created']


class ReservationTimesView(ListView):
    model = Reservation
    template_name = 'reservations/reservation_times.html'
    context_object_name = 'reservations'


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    fields = ['date', 'timeslot', 'court_number']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.all()
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['court_number'].widget = forms.HiddenInput()
        form.fields['date'].widget = forms.HiddenInput()
        return form


def date_form(request):
    return render(request, 'reservations/reservation_date.html')
