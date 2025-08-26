import requests, uuid
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from payment.models import Payment
from payment.forms import PaymentForm
from django.conf import settings
from django.contrib import messages

# Create Views here

# Payment Views
class PaymentListView(ListView):
    model = Payment
    template_name = 'payment/payment_list.html'
    context_object_name = 'payments'
    paginate_by = 10

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment/payment_detail.html'
    context_object_name = 'payment'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment/payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment/payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')


def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            # Generate unique reference ID
            payment.bank_reference_id = str(uuid.uuid4())
            payment.save()

            # Initialize Paystack payment
            headers = {
                'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
                'Content-Type': 'application/json',
            }

            data = {
                'email': payment.email,
                'amount': int(payment.amount * 100),  # Paystack accepts amount in kobo
                'reference': payment.bank_reference_id,
                'callback_url': request.build_absolute_uri('/payment/success/'),
            }

            url = 'https://api.paystack.co/transaction/initialize'
            response = requests.post(url, headers=headers, json=data)
            res_data = response.json()

            if res_data.get('status') is True:
                # Redirect user to Paystack checkout page
                return redirect(res_data['data']['authorization_url'])
            else:
                messages.error(request, 'Error initializing payment. Please try again.')
    else:
        form = PaymentForm()

    return render(request, 'payment/make_payment.html', {'form': form})


def payment_success(request):
    reference = request.GET.get('reference')
    if not reference:
        messages.error(request, 'No reference supplied by Paystack.')
        return redirect('make_payment')

    headers = {
        'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
    }

    url = f'https://api.paystack.co/transaction/verify/{reference}'
    response = requests.get(url, headers=headers)
    res_data = response.json()

    if res_data.get('status') and res_data['data']['status'] == 'success':
        payment = Payment.objects.filter(bank_reference_id=reference).first()
        if payment:
            payment.payment_date = res_data['data']['paid_at']
            payment.remark = 'Payment successful via Paystack'
            payment.save()
        messages.success(request, 'Payment successful!')
        return render(request, 'payment/payment_success.html', {'payment': payment})
    else:
        messages.error(request, 'Payment verification failed.')
        return redirect('make_payment')
    

def payment_history(request):
    payments = Payment.objects.all().order_by('-created_at')  # latest first
    return render(request, 'payment/payment_history.html', {'payments': payments})