from django.contrib import admin
from BuscadorCodigo.models import Actividades

# Register your models here.

class codigosAdmin(admin.ModelAdmin):
    list_display=('codigo', 'nombreActividad')
    search_fields=('codigo', 'nombreActividad')

admin.site.register(Actividades, codigosAdmin)