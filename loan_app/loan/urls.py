from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/search/', views.search, name='transactionid_result')
]