
"""
a custom function that automatically generates emis
"""
from custom.utils import create_emis_for_loan
"""
Import neccessery forms
"""
from user.forms import RegForm, LoginForm
from borrower.forms import BorrowerSubmit
from document.forms import DocumentSubmit
from kyc.forms import KYCSubmit
from loan_ticket.forms import LoanTicketSubmit
from penalty.forms import UserPenaltyForm

"""
import needed modules
"""
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods, require_GET
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils import timezone

"""
Import neccessary models
"""
from penalty.models import Penalty
from borrower.models import Borrower
from document.models import Document
from loan.models import Loan
from kyc.models import KYC
from emi.models import EMI
from loan_ticket.models import LoanTicket

import logging
logger = logging.getLogger(__name__) #logging email error
# Email Verification
"""
Email backend has been implented in settings
import needed modules
"""
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import send_mail
from django.conf import settings
from datetime import date
from dateutil.relativedelta import relativedelta

# Create your views here.

"""
@require_http_methods this allows only GET and POST HTTPrequest to access a logic.
"""
@require_http_methods(["GET", "POST"])
def reg_views(request):
    template_data = {'title': 'Loan Management App'}

    if request.method == "POST":
            form = RegForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False  # inactive until email verification
                user.save()

                # generate activation link
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)
                activation_path = f"/user/activate/account/{uid}/{token}/"
                activation_link = request.build_absolute_uri(activation_path)

                try:
                    send_mail(
                        subject='Loan App Account Activation',
                        message=f'Click the link to verify your account: {activation_link}',
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[user.email],
                        fail_silently=False
                    )
                    messages.info(request, "Account created! Check your email for verification link.")
                    return redirect('email_verify')
                except Exception as e:
                    logger.error(f'Email sending failed for {user.email}: {e}')
                    messages.error(request, "Something went wrong while sending the email.")
            # If form is invalid, it will fall through and re-render below

    else:
        form = RegForm()

    return render(request, 'user/registration.html', {"reg_form": form, "title": template_data['title']})

"""
Logic which controls account activation.
# """
def activate_views(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (Exception, get_user_model().DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, message="Your account is now active, You can login.")
        return redirect("login")
    else:
        messages.error(request, message='Activation link is invalid, Request Another one')
        return redirect('signup')

@require_http_methods(["GET", "POST"])
def login_view(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    if request.method == "GET":
        form = LoginForm()
        return render(request, template_name='user/login.html', context={'login_form':form, 'title':template_data['title']})
    
    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = authenticate(request, email=email, password=password)


        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Invalid Email or Password.")

    return render(request, 'user/login.html', {"login_form": form, 'title':template_data['title']})
    

    ...

"""
On logout and return to homepage.
"""
def logout_view(request):
    logout(request)
    messages.success(request, message='Logout Successful')
    return redirect('home')


@require_GET
def verify_view(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    return render(request, 'user/email_verify.html', {'title':template_data['title']})

@require_http_methods(["GET", "POST"])
@login_required(login_url='login')
def borrower_submit(request):
    template_data = {
        'title' : 'Loan Management App'
    }
    if hasattr(request.user, "borrower"): # Checks if Borrower already exits
        return redirect("document_submit")
    
    if request.method == 'GET':
        form = BorrowerSubmit()
        return render(request, 'user/borrower_submit.html', {'form':form, 'title':template_data['title']})
    
    if request.method == "POST":
        form = BorrowerSubmit(request.POST)
        if form.is_valid():
            borrower = form.save(commit=False)
            borrower.user_profile = request.user  # link borrower to logged-in user
            borrower.save()
            return redirect("document_submit") # redirect after success
    else:
        form = BorrowerSubmit()
    return render(request, "user/borrower_submit.html", {"form": form, 'title':template_data['title']})



@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def kyc_submit(request):
    template_data = {'title': 'Loan Management App'}
    borrower = get_object_or_404(Borrower, user_profile=request.user)

    #  If KYC already exists, skip
    if borrower.kyc_details.exists():
        return redirect("loan_ticket_submit")

    if request.method == 'POST':
        form = KYCSubmit(request.POST, request.FILES)
        if form.is_valid():
            kyc = form.save(commit=False)
            kyc.borrower = borrower
            kyc.save()
            form.save_m2m()
            return redirect("loan_ticket_submit")
    else:
        form = KYCSubmit()

    return render(request, "user/kyc_submit.html", {"form": form, "title": template_data['title']})

@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def document_submit(request):
    template_data = {'title': 'Loan Management App'}
    borrower = get_object_or_404(Borrower, user_profile=request.user)

    # If documents already exist, skip
    if borrower.document_details.exists():
        return redirect("kyc_submit")

    if request.method == "POST":
        form = DocumentSubmit(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.borrower = borrower
            document.save()
            return redirect("kyc_submit")
    else:
        form = DocumentSubmit()

    return render(request, "user/document_submit.html", {"form": form, "title": template_data['title']})


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def loan_ticket_submit(request):
    template_data = {'title': 'Loan Management App'}
    borrower = get_object_or_404(Borrower, user_profile=request.user)

    # If LoanTicket already exists, skip
    if borrower.loanticket_details.exists():
        return redirect("loan_summary")

    if request.method == "POST":
        form = LoanTicketSubmit(request.POST)
        if form.is_valid():
            loan_ticket = form.save(commit=False)
            loan_ticket.borrower = borrower
            loan_ticket.start_date = date.today()

            # Calculate end_date based on tenure
            tenure = loan_ticket.loan_tenure # make sure your form/model has this
            loan_ticket.end_date = loan_ticket.start_date + relativedelta(months=tenure)
            loan_ticket.save()

            #  Auto-create EMIs using the function from utils.py
            create_emis_for_loan(loan_ticket)
            

            return redirect("loan_summary")
    else:
        form = LoanTicketSubmit()

    return render(request, "user/loan_ticket_submit.html", {"form": form, "title": template_data['title']})





@login_required(login_url='login')
def loan_summary(request):
    template_data = {'title': 'Loan Management App'}
    user = request.user
    borrower = get_object_or_404(Borrower, user_profile=user)
    loan = borrower.loanticket_details.last()  # get the latest loan

    # Fetch all EMIs for this loan
    emis = EMI.objects.filter(loan_ticket=loan).order_by('emi_no')

    return render(request, "loan/loan_summary.html", {
        "borrower": borrower,
        "loan": loan,
        "emis": emis,
        'now':timezone.now,
        "title":template_data['title']
    })




@login_required(login_url='login')
def penalty_list(request):
    template_data = {
        'title' : 'Loan Management App'
    }
    borrower = get_object_or_404(Borrower, user_profile=request.user) # Get borrower for logged-in user
    penalties = Penalty.objects.filter(emi__loan_ticket__borrower=borrower)
    return render(request, 'user/penalty_list.html', {'penalties': penalties, 'title':template_data['title']})

@login_required
def penalty_detail(request, pk):
    borrower = get_object_or_404(Borrower, user_profile=request.user)
    penalty = get_object_or_404(Penalty, pk=pk, emi__loan_ticket__borrower=borrower)

    if request.method == "POST":
        form = UserPenaltyForm(request.POST, instance=penalty)
        if form.is_valid():
            form.save()
            return redirect('penalty_list')
    else:
        form = UserPenaltyForm(instance=penalty)

    return render(request, 'user/penalty_detail.html', {
        'penalty': penalty,
        'form': form
    })


"""
User profile which display all the user submited imfomation
"""

@login_required(login_url='login')
def user_profile(request):

    user = request.user

    borrower_info = Borrower.objects.filter(user_profile=user).first()
    if borrower_info:  # make sure borrower exists
        #get all loans for this borrower
        loans = Loan.objects.filter(borrower=borrower_info)
        # get all documents linked to this borrower's loans
        documents = Document.objects.filter(loan__borrower=borrower_info)
    else:
        loans = Loan.objects.none()
        documents = Document.objects.none()
    context = {
        'title':'Loan Managment App',
        'borrower_info': borrower_info,
        'loans': loans,
        'documents': documents,
    }
    return render(request, 'user/profile.html', context)



"""
This logic checks if a user has submitted the required forms after clicking apply for loan, 
if a user logout or was interrupted during any form submition it checks what form has been submitted,
and skips over it. thus improving user experience.
"""
@login_required(login_url='login')
@require_GET
def apply_for_loan(request):
    user = request.user

    # --- Step 1: Borrower ---
    borrower = getattr(user, "borrower", None)
    if not borrower:
        return redirect(reverse("borrower_submit"))

    # --- Step 2: KYC ---
    kyc = KYC.objects.filter(borrower=borrower).first()
    if not kyc:
        return redirect(reverse("kyc_submit"))

    # --- Step 3: Document ---
    document = Document.objects.filter(borrower=borrower).first()
    if not document:  
        return redirect(reverse("document_submit"))

    # --- Step 4: LoanTicket (FK to Borrower) ---
    loan_ticket = LoanTicket.objects.filter(borrower=borrower).first()
    if not loan_ticket:
        return redirect(reverse("loan_ticket_submit"))

    # --- Step 5: EMI (FK to LoanTicket) ---
    if not EMI.objects.filter(loan_ticket=loan_ticket).exists():
        return redirect(reverse("emi_submit"))

    # --- If everything exists ---
    return redirect(reverse("loan_summary")) 
    ...


from rest_framework.decorators import api_view
from rest_framework.response import Response
from custom.services import fetch_nigerian_banks
"""
Gets list of banks with a paystack api key
"""
@api_view(["GET"])
def get_banks(request):
    success, result = fetch_nigerian_banks()

    if success:
        return Response({"banks": result}, status=200)
    return Response({"error": result}, status=404)
