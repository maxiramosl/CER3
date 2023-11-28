from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento, Segmento, Tipo,UsuarioSegmento
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    title = "Inicio"
    tipos= Tipo.objects.all()
    eventos = Evento.objects.all()
    todos=Evento.objects.all()
    segmentos = Segmento.objects.all()
    segmento_filtro = request.GET.get("Segmento")
    tipo_filtro = request.GET.get("Tipo")
    if segmento_filtro==None:
        segmento_filtro='Segmento'
    if tipo_filtro==None:
        tipo_filtro='Tipo'

    
    if (tipo_filtro == 'Tipo' ) and (segmento_filtro == 'Segmento'):
        eventos = Evento.objects.all()
    else:
        if(tipo_filtro != 'Tipo'):
            eventos=Evento.objects.filter(tipo=tipo_filtro)
            print(eventos)
        if(segmento_filtro != 'Segmento'):
            eventos=eventos.filter(segmento=segmento_filtro)

    data = {
        "segmentos":segmentos,
        "tipos":tipos,
        "eventos":eventos,
        "segmento_filtro":segmento_filtro,
        "tipo_filtro":tipo_filtro,
        "title":title,
        "todos":todos,
    }  
    return render(request,'CER3/index.html',data)
