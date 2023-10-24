from django.db import models
# Create your models here.

class CasoAccidente(models.Model):   
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Caso accidente'
        verbose_name_plural = 'Casos accidentes'

    def __str__(self):
        return str(self.nombre)

class TipoAccidente(models.Model):   
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.CharField(max_length=250, verbose_name='Descripcion', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Tipo accidente'
        verbose_name_plural = 'Tipos accidentes'

    def __str__(self):
        return str(self.nombre)

class Accidente(models.Model):
    lesion = models.CharField(max_length=100, verbose_name='Lesion')
    fechaHecho = models.DateTimeField(verbose_name='Fecha Hecho')
    tipoAccidente = models.ForeignKey(TipoAccidente, on_delete=models.CASCADE, null=True)
    casoAccidente = models.ForeignKey(CasoAccidente, on_delete=models.CASCADE, null=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Editado')

    class Meta:
        verbose_name = 'Accidente'
        verbose_name_plural = 'Accidentes'

    def __str__(self):
        return str(self.fechaHecho)

   