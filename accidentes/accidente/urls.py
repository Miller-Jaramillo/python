from django.urls import path
from . import views
urlpatterns = [
    path('cargardatos/',views.cargarExcel, name="cargardatos"),
    path('listaaccidentes/',views.listaAccidentes, name="listaaccidentes"),
    path('encuesta/',views.encuesta, name="encuesta"),
    path('iniciar/',views.iniciar, name="iniciar"),
    path('registrarse/',views.registrarse, name="registrarse"),
    path('dashboard/',views.dashboard, name="dashboard"),
    path('mapa/',views.mapa, name="mapa"),
    path('visual/',views.visual, name="visual"),
    path('analisis/',views.analisis, name="analisis")
    ]
