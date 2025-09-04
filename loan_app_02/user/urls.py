from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.reg_views, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('verify/', views.verify_view, name='email_verify'),
    path('apply/', views.apply_for_loan, name='loan_apply'),
    path('activate/account/<uidb64>/<token>/', views.activate_views, name='activate'),
    path('borrower/submit/', views.borrower_submit, name='borrower_submit'),
    path('kyc/submit/', views.kyc_submit, name='kyc_submit'),
    path('document/submit/', views.document_submit, name='document_submit'),
    path('loan_ticket/submit/', views.loan_ticket_submit, name='loan_ticket_submit'),
    path('penalty/list/', views.penalty_list, name='user_penalty'),
    path('penalties/<int:pk>/', views.penalty_detail, name='user_penalty_detail'),
    path('loan/summary/', views.loan_summary, name='loan_summary'),
    
]