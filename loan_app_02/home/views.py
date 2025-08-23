from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    return render(request, template_name='home/index.html', context={'title':template_data})


def apply_for_loan(request):
    template_data = {}
    template_data['title'] = 'Loan Management App'
    return render(request, template_name='home/loan.html', context={'title':template_data})