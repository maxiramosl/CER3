from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento, Segmento


# Create your views here.
def index(request):
    title = "Inicio"
    eventos = Evento.objects.all()
    segmentos = Segmento.objects.all()
    segmento_filtro = request.GET.get("Segmento")
    evento_filtro = request.GET.get("Tipo")
    print(segmento_filtro)
    
    print(evento_filtro)
    
    if (evento_filtro == 'Tipo' or evento_filtro == None) and (segmento_filtro == 'Segmento' or segmento_filtro == None):
        evento = Evento.objects.all()
    elif(evento_filtro == 'Tipo' or evento_filtro == None) and (segmento_filtro != 'Segmento'):
        a=1
        
    
    
        


        


    data = {
        "segmentos":segmentos,
        "eventos":eventos,
        "segmento_filtro":segmento_filtro,
        "evento_filtro":evento_filtro,
        "title":title
    }  
    return render(request,'CER3/index.html',data)
