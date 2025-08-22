from django.urls import path
from . import views
# LoanTicket URLs
urlpatterns = [
    path('loan_tickets/', views.LoanTicketListView.as_view(), name='loan_ticket_list'),
    path('loan_tickets/<int:pk>/', views.LoanTicketDetailView.as_view(), name='loan_ticket_detail'),
    path('loan_tickets/new/', views.LoanTicketCreateView.as_view(), name='loan_ticket_create'),
    path('loan_tickets/<int:pk>/edit/', views.LoanTicketUpdateView.as_view(), name='loan_ticket_update'),
    path('loan_tickets/<int:pk>/delete/', views.LoanTicketDeleteView.as_view(), name='loan_ticket_delete'),

]