from django.db import models

# Create your models here.

class MapaConceptual(models.Model):
    nombre=models.CharField(max_length=50)
    codigo=models.CharField(primary_key=True, max_length=6)
    
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre,self.codigo)

class Nodo(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    MapaConceptual=models.ForeignKey(MapaConceptual, on_delete = models.CASCADE)
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre,self.codigo) 
        
  

class Evaluacion(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    puntuacion_minima=models.PositiveSmallIntegerField()
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre,self.codigo)

class Ejercicio(models.Model):
    codigo=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=50)
    pregunta=models.CharField(max_length=50)
    Nodo=models.ForeignKey(Nodo, on_delete = models.CASCADE) 
    Evaluacion=models.ForeignKey(Evaluacion, on_delete = models.CASCADE)
    def __str__(self):
     texto="{0} ({1})"
     return texto.format(self.nombre,self.codigo)
