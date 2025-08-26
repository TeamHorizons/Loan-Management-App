from django.urls import path
from . import views
urlpatterns = [
    # Payment URLs
    path('payments/', views.PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', views.PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/new/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/edit/', views.PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),

    # Real Payment Routes
    path('payment/make/', views.make_payment, name='make_payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/history/', views.payment_history, name='payment_history'),
]
