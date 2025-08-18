
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name='index'),

    # Borrower URLs
    path('borrowers/', views.BorrowerListView.as_view(), name='borrower_list'),
    path('borrowers/<int:pk>/', views.BorrowerDetailView.as_view(), name='borrower_detail'),
    path('borrowers/new/', views.BorrowerCreateView.as_view(), name='borrower_create'),
    path('borrowers/<int:pk>/edit/', views.BorrowerUpdateView.as_view(), name='borrower_update'),
    path('borrowers/<int:pk>/delete/', views.BorrowerDeleteView.as_view(), name='borrower_delete'),

    # LoanTicket URLs
    path('loan_tickets/', views.LoanTicketListView.as_view(), name='loan_ticket_list'),
    path('loan_tickets/<int:pk>/', views.LoanTicketDetailView.as_view(), name='loan_ticket_detail'),
    path('loan_tickets/new/', views.LoanTicketCreateView.as_view(), name='loan_ticket_create'),
    path('loan_tickets/<int:pk>/edit/', views.LoanTicketUpdateView.as_view(), name='loan_ticket_update'),
    path('loan_tickets/<int:pk>/delete/', views.LoanTicketDeleteView.as_view(), name='loan_ticket_delete'),

    # EMI URLs
    path('emis/', views.EMIListView.as_view(), name='emi_list'),
    path('emis/<int:pk>/', views.EMIDetailView.as_view(), name='emi_detail'),
    path('emis/new/', views.EMICreateView.as_view(), name='emi_create'),
    path('emis/<int:pk>/edit/', views.EMIUpdateView.as_view(), name='emi_update'),
    path('emis/<int:pk>/delete/', views.EMIDeleteView.as_view(), name='emi_delete'),

    # Document URLs
    path('documents/', views.DocumentListView.as_view(), name='document_list'),
    path('documents/<int:pk>/', views.DocumentDetailView.as_view(), name='document_detail'),
    path('documents/new/', views.DocumentCreateView.as_view(), name='document_create'),
    path('documents/<int:pk>/edit/', views.DocumentUpdateView.as_view(), name='document_update'),
    path('documents/<int:pk>/delete/', views.DocumentDeleteView.as_view(), name='document_delete'),

    # KYC URLs
    path('kyc/', views.KYCListView.as_view(), name='kyc_list'),
    path('kyc/<int:pk>/', views.KYCDetailView.as_view(), name='kyc_detail'),
    path('kyc/new/', views.KYCCreateView.as_view(), name='kyc_create'),
    path('kyc/<int:pk>/edit/', views.KYCUpdateView.as_view(), name='kyc_update'),
    path('kyc/<int:pk>/delete/', views.KYCDeleteView.as_view(), name='kyc_delete'),

    # Penalty URLs
    path('penalties/', views.PenaltyListView.as_view(), name='penalty_list'),
    path('penalties/<int:pk>/', views.PenaltyDetailView.as_view(), name='penalty_detail'),
    path('penalties/new/', views.PenaltyCreateView.as_view(), name='penalty_create'),
    path('penalties/<int:pk>/edit/', views.PenaltyUpdateView.as_view(), name='penalty_update'),
    path('penalties/<int:pk>/delete/', views.PenaltyDeleteView.as_view(), name='penalty_delete'),

    # Payment URLs
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/new/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),
]
