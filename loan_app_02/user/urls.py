from django.urls import path
from user import views
urlpatterns = [
    path('signup/', views.reg_views, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/account/<uidb64>/<token>/', views.activate_views, name='activate'),
]