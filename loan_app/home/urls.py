from django.urls import path
from home import views

# URL goes here

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_dashboard', views.admin_index, name='admin_index'),
    path('admin_dashboard/loan/approved/detail', views.loan_approval_detail, name='loan_approval_detail'),
    path('admin_dashboard/loan/approval/list', views.loan_approval_list, name='loan_approval_list'),
    # path('loans/', views.apply_for_loan, name='next_action')
]
