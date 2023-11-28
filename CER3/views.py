from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento, Segmento, Usuario


# Create your views here.
def index(request):
    title = "Inicio"
    evento = Evento.objects.all()
    segmento = Segmento.objects.all()
    usuario = Usuario.objects.all()
    segmento_filtro = request.GET.get("Segmento")
    evento_filtro = request.GET.get("Tipo")
    #los 2 estan en default
    if((segmento_filtro == 'Segmento' or segmento_filtro is None) and (evento_filtro == 'Tipo' or evento_filtro is None)):
        segmento = Segmento.objects.all()
        evento = Evento.objects.all()
    #el combobox segmento esta en segmento pero el evento no
    elif((segmento_filtro == 'Segmento' or segmento_filtro is None) and (evento_filtro != 'Tipo' or evento_filtro is not None)):
        segmento = Segmento.objects.all()
        evento_filtrado = Evento.objects.get(titulo = evento_filtro)
        evento_filtro = Evento.objects.filter(Evento = evento_filtrado)
    #el combobox de evento esta en defualt pero de segmento no
    elif((segmento_filtro != 'Segmento' or segmento_filtro is not None) and (evento_filtro == 'Tipo' or evento_filtro is None)):
        segmento_filtrado = Segmento.objects.get(nombre = segmento_filtro)
        segmento_filtro = Segmento.objects.filter(Segmento = segmento_filtrado)
        evento = Evento.objects.all()
    elif((segmento_filtro != 'Segmento' or segmento_filtro is not None) and (evento_filtro != 'Tipo' or evento_filtro is not None)):
        evento_filtrado = Evento.objects.get(titulo = evento_filtro)
        evento_filtro = Evento.objects.filter(Evento = evento_filtrado)
        segmento_filtrado = Segmento.objects.get(nombre = segmento_filtro)
        segmento_filtro = Segmento.objects.filter(Segmento = segmento_filtrado)


    data = {
        "segmentos":segmento,
        "eventos":evento,
        "segmento_filtro":segmento_filtro,
        "evento_filtro":evento_filtro,
        "title":title
    }  
    return render(request,'CER3/index.html',data)
