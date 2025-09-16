from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from django.contrib import messages

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Queda en stand by
            user.save()
            messages.success(request, 'Registro enviado. Un administrador debe aprobar tu cuenta.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})