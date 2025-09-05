from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
"""
Import Models
"""
from emi.models import EMI
from borrower.models import Borrower
from loan_ticket.models import LoanTicket


# Create your views here.

# Home View
@staff_member_required(login_url='home')
def admin_index(request):
    """
    Renders the home page of the loan application.
    """
    # You can add some summary data here if needed
    total_borrowers = Borrower.objects.count()
    total_loans = LoanTicket.objects.count()
    ongoing_loans = LoanTicket.objects.filter(status='Ongoing').count()
    pending_emis = EMI.objects.filter(status='Pending').count()

    context = {
        'title': 'Loan Management App',
        'total_borrowers': total_borrowers,
        'total_loans': total_loans,
        'ongoing_loans': ongoing_loans,
        'pending_emis': pending_emis,
    }
    return render(request, 'home/admin.html', context)


def home(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    return render(request, template_name='home/index.html', context={'title':template_data})


@login_required(login_url='login')
def apply_for_loan(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    return render(request, template_name='home/loan.html', context={'title':template_data})