from django.urls import path

from . import views

urlpatterns = [
        # KYC URLs
    path('kycs/', views.KYCListView.as_view(), name='kyc_list'),
    path('kyc/<int:pk>/', views.KYCDetailView.as_view(), name='kyc_detail'),
    path('kyc/new/', views.KYCCreateView.as_view(), name='kyc_create'),
    path('kyc/<int:pk>/edit/', views.KYCUpdateView.as_view(), name='kyc_update'),
    path('kyc/<int:pk>/delete/', views.KYCDeleteView.as_view(), name='kyc_delete'),

]