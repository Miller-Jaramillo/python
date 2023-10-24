from urllib import request
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset 
from accidente.resource import AccidenteResource
from .models import Accidente, TipoAccidente, CasoAccidente
from personas.models import Personas, TipoVictima
from sitios.models import Lugar


# Create your views here.
def list(request):
    
    accidente = Accidente.objects.all()

    tipoAccidente = TipoAccidente.objects.all()

    casoAccidente = CasoAccidente.objects.all()

    personas = Personas.objects.all()

    tipoVictima = TipoVictima.objects.all()

    lugar = Lugar.objects.all()

    return HttpResponse(list)

def cargarExcel(request):
    if request.method == 'POST':  
        accidente_resource = AccidenteResource()  
        nuevos_accidentes = request.FILES['xlsfile']  
        dataset = Dataset()
        import_datos=dataset.load(nuevos_accidentes.read())
        for datos in import_datos:
            
            taccidente = TipoAccidente(
                nombre = datos[8]
            )  
            caccidente = CasoAccidente(
                nombre = datos[9],
            )
            aaccidente = Accidente(

                lesion = datos[10],
                hipotesis = datos[11],
                fechaHecho = datos[0],
                TipoAccidente = taccidente,
                CasoAccidente = caccidente

            )
            ppersonas = Personas(
                edad = datos[5],
                genero = datos[6],
                tipoVictima = datos[7]

            )
            victima = TipoVictima(
                 nombre = datos[7]
            )
            llugar = Lugar(
                comuna = datos[3],
                lugar = datos[2],
                direccion = datos[1],
                divisionPostal = datos[4]
            )

            taccidente.save()  
            caccidente.save()
            aaccidente.save()
            ppersonas.save()
            victima.save()
            llugar.save() 

    return render(request, 'accidente/cargarDatos.html')
 
def listaAccidentes(request):
    accidente = Accidente.objects.all()
    casoacc = CasoAccidente.objects.all()
    tipoacc = TipoAccidente.objects.all()
    personas = Personas.objects.all()
    tipovic = TipoVictima.objects.all()
    lugar = Lugar.objects.all()
  #  lista = list(accidente) + list(casoacc) + list(tipoacc) + list(personas) + list(tipovic) + list(lugar)

    matriz = [
        [accidente, casoacc, tipoacc ],
        [personas, tipovic, lugar],
    ]
    return render(request, 'accidente/listaAccidentes.html',{"accidente":accidente, "casoacc":casoacc, "tipoac":tipoacc, "personas":personas, "tipovic":tipovic, "lugar":lugar, "matriz":matriz})

def encuesta(request):
    return render(request, 'accidente/encuesta.html')

def iniciar(request):
    return render(request, 'accidente/iniciar.html')

def registrarse(request):
    return render(request, 'accidente/registrarse.html')

def consultas(request):
    return render(request, 'accidente/consultas.html')
    lesion = Accidente.objects.filter(lesion="CABEZA")
    edad = Personas.objects.filter(edad__gte=30)
    edad = Personas.objects.filter(edad__lte=30)
    casoLetraF = Accidente.objects.filter(casoAccidente__startswith='F')
    casoLetraF = Accidente.objects.filter(casoAccidente__contains='H')
    lugarLetraP = Lugar.objects.filter(lugar__startswith='P')
def visual(request):
    return render(request, 'accidente/visual.html')
def dashboard(request):
    return render(request, 'accidente/dashboard.html')
def mapa(request):

    return render(request, 'accidente/mapa.html')
def analisis(request):

    return render(request, 'accidente/analisis.html')