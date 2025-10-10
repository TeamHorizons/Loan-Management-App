
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from loan_ticket.models import LoanTicket, LoanSettings
from loan_ticket.forms import LoanTicketForm
from django.shortcuts import render
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


"""
Loan Settings View logic
"""

class LoanSettingsCreateView(CreateView):
    model = LoanSettings
    fields = ['interest_rate']
    template_name = 'loan_ticket/loansettings_form.html'
    success_url = reverse_lazy('admin_index')

class LoanSettingsUpdateView(UpdateView):
    model = LoanSettings
    fields = ['interest_rate']
    template_name = 'loan_ticket/loansettings_form.html'
    success_url = reverse_lazy('admin_index')

class LoanSettingsDeleteView(DeleteView):
    model = LoanSettings
    template_name = 'loan_ticket/loansettings_confirm_delete.html'
    success_url = reverse_lazy('admin_index')


def loan_settings_dashboard(request):
    settings = LoanSettings.objects.last()  # Get latest (or None if doesn't exist)
    return render(request, 'home/admin.html', {"settings": settings})