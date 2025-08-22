from django.shortcuts import render



from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from loan_ticket.models import LoanTicket
from loan_ticket.forms import LoanTicketForm

# Create your views here.


# LoanTicket Views
class LoanTicketListView(ListView):
    model = LoanTicket
    template_name = 'loan_ticket/loan_ticket_list.html'
    context_object_name = 'loan_tickets'
    paginate_by = 10

class LoanTicketDetailView(DetailView):
    model = LoanTicket
    template_name = 'loan_ticket/loan_ticket_detail.html'
    context_object_name = 'loan_ticket'

class LoanTicketCreateView(CreateView):
    model = LoanTicket
    form_class = LoanTicketForm
    template_name = 'loan_ticket/loan_ticket_form.html'
    success_url = reverse_lazy('loan_ticket_list')

class LoanTicketUpdateView(UpdateView):
    model = LoanTicket
    form_class = LoanTicketForm
    template_name = 'loan_ticket/loan_ticket_form.html'
    success_url = reverse_lazy('loan_ticket_list')

class LoanTicketDeleteView(DeleteView):
    model = LoanTicket
    template_name = 'loan_ticket/loan_ticket_confirm_delete.html'
    success_url = reverse_lazy('loan_ticket_list')
