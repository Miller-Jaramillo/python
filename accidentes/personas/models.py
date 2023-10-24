from django.db import models

# Create your models here.

class Personas(models.Model):   
    edad = models.CharField(max_length=100, verbose_name='Edad')
    genero = models.CharField(max_length=50, verbose_name='Genero', null=True, blank=True)
    tipoVictima = models.CharField(max_length=50, verbose_name='Tipo victima', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Personas'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return str(self.edad)

class TipoVictima(models.Model):   
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Tipo victima'
        verbose_name_plural = 'Tipos victimas'

    def __str__(self):
        return str(self.nombre)

