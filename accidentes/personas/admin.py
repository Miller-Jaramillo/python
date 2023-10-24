from django.contrib import admin
from .models import Personas, TipoVictima

# Register your models here.
class PersonasAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('edad', 'genero', 'tipoVictima',)
    list_display = ('edad', 'genero', 'tipoVictima', 'create_at', 'update_at',)
    ordering = ('-create_at',)

admin.site.register(Personas, PersonasAdmin)

class TipoVictimaAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('nombre', 'descripcion',)
    list_display = ('nombre','descripcion', 'create_at', 'update_at',)
    ordering = ('-create_at',)

admin.site.register(TipoVictima, TipoVictimaAdmin)