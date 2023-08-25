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


class ReservationListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
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

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class ReservationUserListView(LoginRequiredMixin, ListView):
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


class ReservationCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    CreateView
        ):
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
        reservation_date = self.request.POST.get('date')
        reservation_timeslot = self.request.POST.get('timeslot')
        reservation_court_number = self.request.POST.get('court_number')

        if reservation_timeslot == '0':
            reservation_timeslot = '9:00'
        elif reservation_timeslot == '1':
            reservation_timeslot = '10:00'
        elif reservation_timeslot == '2':
            reservation_timeslot = '11:00'
        elif reservation_timeslot == '3':
            reservation_timeslot = '12:00'
        elif reservation_timeslot == '4':
            reservation_timeslot = '13:00'
        elif reservation_timeslot == '5':
            reservation_timeslot = '14:00'
        elif reservation_timeslot == '6':
            reservation_timeslot = '15:00'
        elif reservation_timeslot == '7':
            reservation_timeslot = '16:00'
        elif reservation_timeslot == '8':
            reservation_timeslot = '17:00'
        elif reservation_timeslot == '9':
            reservation_timeslot = '18:00'
        elif reservation_timeslot == '10':
            reservation_timeslot = '19:00'
        elif reservation_timeslot == '11':
            reservation_timeslot = '20:00'

        court_number_correct = (int(reservation_court_number) + 1)

        send_mail(
            'Bushy Park Tennis Club - Reservation Confirmation',  # SUBJECT
            f'Hi {self.request.user.first_name}, \nThis is an email'  # BODY
            f' confirmation of your court reservation at'
            f' Bushy Park Tennis Club. \n\n'
            f'\n -- RESERVATION DETAILS --\n\n'
            f'DATE: {reservation_date}\n'
            f'TIME: {reservation_timeslot} \n'
            f'COURT: {court_number_correct}'
            f'\n\nIf you need to cancel this reservation, please log in'
            f'to your account on our site and click "My Reservations".'
            f'\n\nWe look forward to seeing you at the club!',
            'from@yourdjangoapp.com',  # FROM (OVERRIDDEN)
            [self.request.user.email],  # TO
            fail_silently=False,
        )
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['court_number'].widget = forms.HiddenInput()
        form.fields['date'].widget = forms.HiddenInput()
        return form


class ReservationDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    SuccessMessageMixin,
    DeleteView
        ):
    model = Reservation
    success_url = reverse_lazy('reservation-user-list')
    success_message = (
        'Your reservation has been cancelled.'
    )

    def test_func(self):
        reservation = self.get_object()
        if self.request.user == reservation.created_by:
            return True
        elif self.request.user.is_staff:
            return True
        return False

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(
            ReservationDeleteView, self
            ).delete(request, *args, **kwargs)


def date_form(request):
    return render(request, 'reservations/reservation_date.html')
