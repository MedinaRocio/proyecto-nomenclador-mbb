from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

from BuscadorCodigo.models import Actividades

# Vista de BOTON BUSCAR

def boton_buscar(request):
    
    if request.GET["buscar"]: # Determina si se ingreso algo en la caja de busqueda
    
        busqueda_ingresada=request.GET["buscar"] 
        
        if len(busqueda_ingresada) > 500: 
            mostrar_mensaje="El texto ingresado es demasiado largo."
            
        elif busqueda_ingresada==int:  
        
            actividad=Actividades.objects.filter(codigo__icontains=busqueda_ingresada) 
            
        else:
            actividad=Actividades.objects.filter(nombreActividad__icontains=busqueda_ingresada) 
        
            return render(request, 'resultados_busqueda.html' , {"actividad":actividad , "query":busqueda_ingresada}) 
    
    else:
        
        mostrar_mensaje= "Debe ingresar alguna busqueda" 
    
    return HttpResponse(mostrar_mensaje)


def volver(request):
    if request.method == 'POST':
        return render(request, 'principal.html')

