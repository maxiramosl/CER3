from CER3.models import Evento
from rest_framework import serializers

class SerializadorEvento(serializers.ModelSerializer):
    
    class Meta:
        model = Evento
        fields = '__all__' 
        #['fecha_inicio', 'fecha_termino', 'titulo', 'descripcion','tipo','segmento']