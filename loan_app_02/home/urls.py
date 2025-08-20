from django.urls import path
from home import views

# URL goes here

urlpatterns = [
    path('', views.home, name='home'),
    path('loans/', views.apply_for_loan, name='next_action')
]