from django.db.models import Func, F, Value
from django.db.models.functions import Replace
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TempEpisodioAdmision
from django.db.models.functions import Right


@login_required
def home(request):
    dni = request.GET.get('dni', '').strip()
    resultados = []

    if dni.isdigit() and len(dni) == 8:
        resultados = TempEpisodioAdmision.objects.annotate(
            dni_recortado=Right('id_paciente', 8)
        ).filter(dni_recortado=dni)

    return render(request, 'home.html', {
        'dni': dni,
        'resultados': resultados
    })
