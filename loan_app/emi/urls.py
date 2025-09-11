from django.urls import path
from . import views
urlpatterns = [
        # EMI URLs
    path('emis/', views.EMIListView.as_view(), name='emi_list'),
    path('emis/<int:pk>/', views.EMIDetailView.as_view(), name='emi_detail'),
    path('emis/new/', views.EMICreateView.as_view(), name='emi_create'),
    path('emis/<int:pk>/edit/', views.EMIUpdateView.as_view(), name='emi_update'),
    path('emis/<int:pk>/delete/', views.EMIDeleteView.as_view(), name='emi_delete'),

]