from django.db import models

# Create your models here.


class Lugar(models.Model):   
    divisionPostal = models.CharField(max_length=20, verbose_name='Codigo postal', null=True, blank=True)
    comuna = models.CharField(max_length=15, verbose_name='Comuna', null=True, blank=True)
    lugar = models.CharField(max_length=100, verbose_name='Lugar', null=True, blank=True)
    direccion = models.CharField(max_length=100, verbose_name='Direccion', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'

    def __str__(self):
        return str(self.divisionPostal)

