from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Accidente, CasoAccidente, TipoAccidente


# Register your models here.
class AccidenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('lesion', 'fechaHecho', 'tipoAccidente__nombre',)
    list_display = ('lesion','fechaHecho', 'create_at', 'update_at',)
    ordering = ('-create_at',)
  

admin.site.register(Accidente, AccidenteAdmin)



class CasoAccidenteAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('nombre', 'descripcion',)
    list_display = ('nombre','descripcion', 'create_at', 'update_at',)
    ordering = ('-create_at',)

admin.site.register(CasoAccidente, CasoAccidenteAdmin)

class TipoAccidenteAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('nombre', 'descripcion',)
    list_display = ('nombre','descripcion', 'create_at', 'update_at',)
    ordering = ('-create_at',)

admin.site.register(TipoAccidente, TipoAccidenteAdmin)

