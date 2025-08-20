from django.shortcuts import render, redirect
from user.forms import RegForm, LoginForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from django.views.decorators.http import require_http_methods
import logging

logger = logging.getLogger(__name__)
# Email Verification
"""
Email backend has been implented in settings
"""
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

"""
@require_http_methods this allows only GET and POST HTTPrequest to access a logic.
"""
@require_http_methods(["GET", "POST"])
def reg_views(request):
        template_data = {}
        template_data['title'] = 'Loan Management App'
        if request.method == "GET":
            form = RegForm()
            return render(request, template_name='user/registration.html', context={"reg_form":form, "title":template_data})

        #Post request after form submition
        form = RegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_path = f"/user/activate/account/{uid}/{token}/"
            activation_link =  request.build_absolute_uri(activation_path)

            try:
                send_mail(
                    subject='Loan App Account Activation',
                    message=f'Click the link to verify your account: {activation_link}',
                    from_email= settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],
                    fail_silently=False
                )
                messages.success(request, message="Account Created! Check email to activate. If not seen check spam box.")
                return redirect(to='login')
            except Exception as e:
                logger.error(f'Email sending failed for {user.email}:{e}')
                messages.error(request, message=f'Something went wrong.')
        else:
            return render(request, template_name='user/registration.html', context={'reg_form':form})

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
        messages.success(request, message="Your account is now active.")
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
        return render(request, template_name='user/login.html', context={'login_form':form, 'title':template_data})
    
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

    return render(request, 'user/login.html', {"login_form": form, 'title':template_data})
    

    ...

"""
On logout and return to homepage.
"""
def logout_view(request):
    logout(request)
    messages.success(request, message='Logout Successful')
    return redirect('home')