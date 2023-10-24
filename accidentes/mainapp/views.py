from django.shortcuts import render

from accidente.models import Accidente, CasoAccidente, TipoAccidente
from personas.models import Personas, TipoVictima
from sitios.models import Lugar

# Create your views here.
def iniciar(request):
    return render(request, 'mainapp/iniciar.html',{
    })  
