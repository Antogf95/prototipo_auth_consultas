from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import EstiloLoginForm




urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html', authentication_form=EstiloLoginForm), name='login'),


]