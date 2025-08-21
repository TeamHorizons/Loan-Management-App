
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Borrower, LoanTicket, EMI, Document, KYC, Penalty, Payment
from .forms import (
    BorrowerForm, LoanTicketForm, EMIForm, DocumentForm, KYCForm, PenaltyForm, PaymentForm
)

# Home View
def index(request):
    """
    Renders the home page of the loan application.
    """
    # You can add some summary data here if needed
    total_borrowers = Borrower.objects.count()
    total_loans = LoanTicket.objects.count()
    ongoing_loans = LoanTicket.objects.filter(status='Ongoing').count()
    pending_emis = EMI.objects.filter(status='Pending').count()

    context = {
        'total_borrowers': total_borrowers,
        'total_loans': total_loans,
        'ongoing_loans': ongoing_loans,
        'pending_emis': pending_emis,
    }
    return render(request, 'loan_app/index.html', context)

# Borrower Views
class BorrowerListView(ListView):
    model = Borrower
    template_name = 'loan_app/borrower_list.html'
    context_object_name = 'borrowers'
    paginate_by = 10

class BorrowerDetailView(DetailView):
    model = Borrower
    template_name = 'loan_app/borrower_detail.html'
    context_object_name = 'borrower'

class BorrowerCreateView(CreateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = 'loan_app/borrower_form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerUpdateView(UpdateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = 'loan_app/borrower_form.html'
    success_url = reverse_lazy('borrower_list')

class BorrowerDeleteView(DeleteView):
    model = Borrower
    template_name = 'loan_app/borrower_confirm_delete.html' # Create this template
    success_url = reverse_lazy('borrower_list')

# LoanTicket Views
class LoanTicketListView(ListView):
    model = LoanTicket
    template_name = 'loan_app/loan_ticket_list.html'
    context_object_name = 'loan_tickets'
    paginate_by = 10

class LoanTicketDetailView(DetailView):
    model = LoanTicket
    template_name = 'loan_app/loan_ticket_detail.html'
    context_object_name = 'loan_ticket'

class LoanTicketCreateView(CreateView):
    model = LoanTicket
    form_class = LoanTicketForm
    template_name = 'loan_app/loan_ticket_form.html'
    success_url = reverse_lazy('loan_ticket_list')

class LoanTicketUpdateView(UpdateView):
    model = LoanTicket
    form_class = LoanTicketForm
    template_name = 'loan_app/loan_ticket_form.html'
    success_url = reverse_lazy('loan_ticket_list')

class LoanTicketDeleteView(DeleteView):
    model = LoanTicket
    template_name = 'loan_app/loan_ticket_confirm_delete.html'
    success_url = reverse_lazy('loan_ticket_list')

# EMI Views
class EMIListView(ListView):
    model = EMI
    template_name = 'loan_app/emi_list.html'
    context_object_name = 'emis'
    paginate_by = 10

class EMIDetailView(DetailView):
    model = EMI
    template_name = 'loan_app/emi_detail.html'
    context_object_name = 'emi'

class EMICreateView(CreateView):
    model = EMI
    form_class = EMIForm
    template_name = 'loan_app/emi_form.html'
    success_url = reverse_lazy('emi_list')

class EMIUpdateView(UpdateView):
    model = EMI
    form_class = EMIForm
    template_name = 'loan_app/emi_form.html'
    success_url = reverse_lazy('emi_list')

class EMIDeleteView(DeleteView):
    model = EMI
    template_name = 'loan_app/emi_confirm_delete.html'
    success_url = reverse_lazy('emi_list')

# Document Views
class DocumentListView(ListView):
    model = Document
    template_name = 'loan_app/document_list.html'
    context_object_name = 'documents'
    paginate_by = 10

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'loan_app/document_detail.html'
    context_object_name = 'document'

class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'loan_app/document_form.html'
    success_url = reverse_lazy('document_list')

class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'loan_app/document_form.html'
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'loan_app/document_confirm_delete.html'
    success_url = reverse_lazy('document_list')

# KYC Views
class KYCListView(ListView):
    model = KYC
    template_name = 'loan_app/kyc_list.html'
    context_object_name = 'kycs'
    paginate_by = 10

class KYCDetailView(DetailView):
    model = KYC
    template_name = 'loan_app/kyc_detail.html'
    context_object_name = 'kyc'

class KYCCreateView(CreateView):
    model = KYC
    form_class = KYCForm
    template_name = 'loan_app/kyc_form.html'
    success_url = reverse_lazy('kyc_list')

class KYCUpdateView(UpdateView):
    model = KYC
    form_class = KYCForm
    template_name = 'loan_app/kyc_form.html'
    success_url = reverse_lazy('kyc_list')

class KYCDeleteView(DeleteView):
    model = KYC
    template_name = 'loan_app/kyc_confirm_delete.html'
    success_url = reverse_lazy('kyc_list')

# Penalty Views
class PenaltyListView(ListView):
    model = Penalty
    template_name = 'loan_app/penalty_list.html'
    context_object_name = 'penalties'
    paginate_by = 10

class PenaltyDetailView(DetailView):
    model = Penalty
    template_name = 'loan_app/penalty_detail.html'
    context_object_name = 'penalty'

class PenaltyCreateView(CreateView):
    model = Penalty
    form_class = PenaltyForm
    template_name = 'loan_app/penalty_form.html'
    success_url = reverse_lazy('penalty_list')

class PenaltyUpdateView(UpdateView):
    model = Penalty
    form_class = PenaltyForm
    template_name = 'loan_app/penalty_form.html'
    success_url = reverse_lazy('penalty_list')

class PenaltyDeleteView(DeleteView):
    model = Penalty
    template_name = 'loan_app/penalty_confirm_delete.html'
    success_url = reverse_lazy('penalty_list')

# Payment Views
class PaymentListView(ListView):
    model = Payment
    template_name = 'loan_app/payment_list.html'
    context_object_name = 'payments'
    paginate_by = 10

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'loan_app/payment_detail.html'
    context_object_name = 'payment'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'loan_app/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'loan_app/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'loan_app/payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')

