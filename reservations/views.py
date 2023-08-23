from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
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
    ordering = ['-date', 'timeslot']
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


class ReservationUserListView(ListView):
    model = Reservation
    template_name = 'reservations/reservation_user_list.html'
    context_object_name = 'reservations'
    ordering = ['date', 'timeslot']
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        context = super().get_context_data(**kwargs)
        context['reservations'] = context['reservations'].filter(
            date__gte=today
        )
        return context


class ReservationDetailView(DetailView):
    model = Reservation


class ReservationTimesView(ListView):
    model = Reservation
    template_name = 'reservations/reservation_times.html'
    context_object_name = 'reservations'


class ReservationCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Reservation
    fields = ['date', 'timeslot', 'court_number']
    success_url = reverse_lazy('reservation-user-list')
    success_message = (
        'Your reservation has been made successfully. You will'
        ' receive a confirmation email shortly.'
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reservations"] = Reservation.objects.all()
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        send_mail(
            'Bushy Park Tennis Club - Reservation Confirmation',
            f'Hi {self.request.user.first_name}, This is an email confirmation.'
            f'Booking Details: {object.date} - {object.timeslot} - {object.court_number}',
            f'Booking Details: {reservation.date} - {reservation.timeslot} - {reservation.court_number}',
            'from@yourdjangoapp.com',
            [self.request.user.email],
            fail_silently=False,
        )
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
