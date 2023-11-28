from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from API import serializer
from CER3.models import UsuarioSegmento, Evento,Segmento
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter

class permiso(permissions.BasePermission):
    def has_permission(self, request, view):
        relacion=UsuarioSegmento.objects.all()
        nombreUsuario=request.user.username
        if relacion.filter(usuarios=request.user)== Segmento.objects.filter(nombre='desarrollador'):
            return True
        else :
            return False
        

            


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all().order_by('fecha_inicio')
    serializer_class = serializer.SerializadorEvento
    permission_classes = [permiso]
    filter_backends=[SearchFilter]
    search_fields = ['segmento__nombre', 'tipo__nombre','fecha_inicio']

    

# Create your views here.
