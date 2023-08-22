from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )
from django.urls import reverse_lazy
from .models import Reservation
import datetime


class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservations/reservation_list.html'
    context_object_name = 'reservations'
    ordering = ['date']
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ----- Date Search -----
        date_search_input = self.request.GET.get('date-search') or ''
        if date_search_input:
            context['reservations'] = context['reservations'].filter(
                date=date_search_input
            )
        context['date_search_input'] = date_search_input

        # ----- Timeslot Search -----
        timeslot_search_input = self.request.GET.get('timeslot-search') or ''
        if timeslot_search_input:
            context['reservations'] = context['reservations'].filter(
                timeslot=timeslot_search_input
            )
        context['timeslot_search_input'] = timeslot_search_input

        # ----- Name Search -----
        name_search_input = self.request.GET.get('name-search') or ''
        if name_search_input:
            context['reservations'] = context['reservations'].filter(
                created_by__last_name__icontains=name_search_input
            )
        context['name_search_input'] = name_search_input

        return context


class ReservationDetailView(DetailView):
    model = Reservation


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


class ReservationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Reservation
    success_url = reverse_lazy('reservation-list')

    def test_func(self):
        reservation = self.get_object()
        if self.request.user == reservation.created_by:
            return True
        elif self.request.user.is_staff:
            return True
        return False


def date_form(request):
    return render(request, 'reservations/reservation_date.html')
