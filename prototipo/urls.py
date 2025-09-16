from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # esto conecta las URLs de login/logout
    path('', include('consultas.urls'))

]
