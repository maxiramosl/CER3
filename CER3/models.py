from django.db import models
from django.contrib.auth.models import User

class Segmento(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True)
    def __str__(self) -> str:
        return self.nombre


class Evento (models.Model):
    fecha_inicio=models.DateField()
    fecha_termino=models.DateField()
    titulo=models.CharField(max_length=30, primary_key=True)
    descripcion=models.TextField()
    tipo=[ ("Vacaciones"),
          ("Feriado"),
          ("Suspension de Actividades"),
          ("Suspension de actividades PM"),
          ("Periodo Lectivo"),
          ("Suspension de evaluaciones"),
          ("Ceremonia"),
          ("EDDA"),
          ("Evaluacion"),
          ("Ayudantias"),
          ("Hito Academico"),
          ("Secretaria Academica"),
          ("OAI"),
    ]
    segmento=models.ManyToManyField(Segmento)
    def __str__(self) -> str:
        return self.titulo
    
class Usuario(models.Model):
    nombre=models.CharField(max_length=30, primary_key=True)
    segmento=models.ForeignKey(Segmento, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre











