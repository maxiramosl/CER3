from django.db import models
from django.contrib.auth.models import User

class Segmento(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True, default="")
    
    def getNombre(self) -> str:
        return self.nombre
    def __str__(self) -> str:
        return self.nombre
    
class Tipo(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True, default="")
    def __str__(self) -> str:
        return self.nombre

class Evento (models.Model):
    hit = models.IntegerField(default = 0)
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    titulo=models.CharField(max_length=30, primary_key=True)
    descripcion=models.TextField()
    tipo=models.OneToOneField(Tipo, on_delete=models.CASCADE)
    segmento=models.ManyToManyField(Segmento)
    def __str__(self) -> str:
        return self.titulo
    
class UsuarioSegmento(models.Model):
    usuarios=models.OneToOneField(User, on_delete=models.CASCADE)
    segmento=models.ForeignKey(Segmento, on_delete=models.CASCADE)
    def getSegmento(self) ->str:
        return self.segmento
    

    










