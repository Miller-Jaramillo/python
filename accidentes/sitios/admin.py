from django.contrib import admin
from .models import Lugar

# Register your models here.
class LugarAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at',)
    search_fields = ('divisionPostal', 'comuna', 'lugar', 'direccion',)
    list_display = ('divisionPostal','comuna', 'lugar', 'direccion', 'create_at', 'update_at',)
    ordering = ('-create_at',)

admin.site.register(Lugar, LugarAdmin)

