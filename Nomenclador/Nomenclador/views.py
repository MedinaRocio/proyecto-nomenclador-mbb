from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render


def inicio(request): 
    
    return render(request, 'principal.html', {"+ BUSQUEDA ASISTIDA SECUENCIAL":2, "+ BUSQUEDA POR CODIGO DE ACTIVIDAD O PALABRA CLAVE": 3, "+ DESCARGAR ARCHIVO COMPLETO":4})


