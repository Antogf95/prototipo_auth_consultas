from django.contrib import admin
from django.urls import path, include
from consultas.views import consultar_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # esto conecta las URLs de login/logout
    path('home/', consultar_home, name="home")

]
