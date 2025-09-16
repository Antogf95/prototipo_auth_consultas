from django.db.models import Func, F, Value
from django.db.models.functions import Replace
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Episodio


@login_required
def home(request):
    dni = request.GET.get('dni', '').strip()
    episodios = []

    if dni:
        episodios = Episodio.objects.select_related('paciente', 'medico').filter(
            paciente__dni__icontains=dni
        )

    return render(request, 'home.html', {
        'dni': dni,
        'episodios': episodios
    })
