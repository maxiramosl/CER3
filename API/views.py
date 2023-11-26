from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from API import serializer
from CER3 import models



class EventoViewSet(viewsets.ModelViewSet):

    queryset = models.Evento.objects.all().order_by('fecha_inicio')
    serializer_class = serializer.SerializadorEvento
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.
