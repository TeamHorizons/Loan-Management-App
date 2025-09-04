from django.urls import path
from . import views
urlpatterns = [
    # Penalty URLs
    path('penalties/', views.PenaltyListView.as_view(), name='penalty_list'),
    path('penalties/<int:pk>/', views.PenaltyDetailView.as_view(), name='penalty_detail'),
    path('penalties/new/', views.PenaltyCreateView.as_view(), name='penalty_create'),
    path('penalties/<int:pk>/edit/', views.PenaltyUpdateView.as_view(), name='penalty_update'),
    path('penalties/<int:pk>/delete/', views.PenaltyDeleteView.as_view(), name='penalty_delete'),
]