
from django.urls import path

from . import views

# Borrower URLs
urlpatterns = [
    path('borrowers/', views.BorrowerListView.as_view(), name='borrower_list'),
    path('borrowers/<int:pk>/', views.BorrowerDetailView.as_view(), name='borrower_detail'),
    path('borrowers/new/', views.BorrowerCreateView.as_view(), name='borrower_create'),
    path('borrowers/<int:pk>/edit/', views.BorrowerUpdateView.as_view(), name='borrower_update'),
    path('borrowers/<int:pk>/delete/', views.BorrowerDeleteView.as_view(), name='borrower_delete'),

]