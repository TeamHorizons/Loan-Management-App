"""
URL configuration for loan_app_02 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('user/', include("user.urls")),
    path('manage/borrower/', include("borrower.urls")),
    path('manage/document/', include("document.urls")),
    path('manage/kyc/', include("kyc.urls")),
    path('manage/emi/', include("emi.urls")),
    path('manage/loan_ticket/', include("loan_ticket.urls")),
    path('manage/payment/', include("payment.urls")),
    path('manage/penalty/', include("penalty.urls")),
]
