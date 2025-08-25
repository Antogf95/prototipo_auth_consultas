import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def consultar_home(request):
    # Cantidad de usuarios a solicitar (por defecto 1)
    cantidad = request.GET.get('results', 1)

    # Llamada a la API
    url = f'https://randomuser.me/api/?results={cantidad}'
    response = requests.get(url)
    data = response.json() if response.status_code == 200 else {}

    # Extraemos la lista de usuarios (clave "results")
    usuarios = data.get('results', [])

    return render(request, 'home.html', {
        'usuarios': usuarios,
        'cantidad': cantidad,
    })
