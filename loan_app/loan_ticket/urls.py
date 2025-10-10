from django.urls import path
from . import views
# LoanTicket URLs
urlpatterns = [
    path('loan_tickets/', views.LoanTicketListView.as_view(), name='loan_ticket_list'),
    path('loan_tickets/<int:pk>/', views.LoanTicketDetailView.as_view(), name='loan_ticket_detail'),
    path('loan_tickets/new/', views.LoanTicketCreateView.as_view(), name='loan_ticket_create'),
    path('loan_tickets/<int:pk>/edit/', views.LoanTicketUpdateView.as_view(), name='loan_ticket_update'),
    path('loan_tickets/<int:pk>/delete/', views.LoanTicketDeleteView.as_view(), name='loan_ticket_delete'),
    
    path('loan_settings/rate/', views.LoanSettingsCreateView.as_view(), name="change_loan_rate"),
    path('loan_settings/update/<int:pk>/', views.LoanSettingsUpdateView.as_view(), name="update_loan_rate"),
    path('loan_settings/delete/<int:pk>/', views.LoanSettingsDeleteView.as_view(), name='delete_loan_rate'),

]