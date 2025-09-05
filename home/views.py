from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
"""
Import Models
"""
from emi.models import EMI
from borrower.models import Borrower
from loan_ticket.models import LoanTicket
from loan.models import Loan

# Create your views here.

# Home View
@staff_member_required(login_url='login')
def admin_index(request):
    """
    Renders the home page of the loan application.
    """
    # You can add some summary data here if needed
    total_borrowers = Borrower.objects.count()
    total_loans = LoanTicket.objects.count()
    ongoing_loans = LoanTicket.objects.filter(status='Ongoing').count()
    pending_emis = EMI.objects.filter(status='Pending').count()
    pending_loans = Loan.objects.filter(status="PENDING").count()  # for new card


    context = {
        'title': 'Loan Management App',
        'total_borrowers': total_borrowers,
        'total_loans': total_loans,
        'ongoing_loans': ongoing_loans,
        'pending_emis': pending_emis,
        "pending_loans": pending_loans,
    }
    return render(request, 'home/admin.html', context)


@staff_member_required(login_url='login')
@login_required
def loan_approval_list(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    loans = Loan.objects.filter(status="PENDING")
    return render(request, "home/loan_approval.html", {"loans": loans, 'title':template_data['title']})


@staff_member_required(login_url='login')
@login_required
def loan_approval_detail(request, pk):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    loan = get_object_or_404(Loan, pk=pk)
    
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "approve":
            loan.status = "APPROVED"
        elif action == "reject":
            loan.status = "REJECTED"
        loan.save()
        return redirect("loan_approval_list")
    
    return render(request, "home/loan_approval.html", {"loan": loan, 'title':template_data['title']})


def home(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    return render(request, template_name='home/index.html', context={'title':template_data['title']})
