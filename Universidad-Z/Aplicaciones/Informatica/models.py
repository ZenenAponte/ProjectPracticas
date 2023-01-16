from django.db import models

# Create your models here.

class Categoria (models.Model):
    idCat=models.CharField(primary_key=True, max_length=4)
    tipoCat=models.CharField(max_length=20)
    
    def __str__(self):
        texto="({0}) {1}"
        return texto.format(self.idCat, self.tipoCat)

class Contrato (models.Model):
    idCont=models.CharField(primary_key=True, max_length=4)
    tipoCont=models.CharField(max_length=20)

    def __str__(self):
        texto="({0}) {1}"
        return texto.format(self.idCont, self.tipoCont)

class Maestria (models.Model):
    idMae=models.CharField(primary_key=True, max_length=4)
    tipoMae=models.CharField(max_length=20)
    
    def __str__(self):
        texto="({0}) {1}"
        return texto.format(self.idMae, self.tipoMae)

class Doctorado (models.Model):
    idDoc=models.CharField(primary_key=True, max_length=4)
    tipoDoc=models.CharField(max_length=20)

    def __str__(self):
        texto="({0}) {1}"
        return texto.format(self.idDoc, self.tipoDoc)

class Profesor (models.Model):
    dni=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=25)
    primerApellido=models.CharField(max_length=25)
    segundoApellido=models.CharField(max_length=25)
    sexo=models.CharField(max_length=10)
    numNomina=models.IntegerField()
    fechaIngreso=models.DateField()
    estado=models.CharField(max_length=20)
    departamento=models.CharField(max_length=20)
    Categoria=models.ForeignKey(Categoria, on_delete = models.CASCADE)
    Contrato=models.ForeignKey(Contrato, on_delete = models.CASCADE)
    Maestria=models.ForeignKey(Maestria, null=True, blank=True, on_delete = models.CASCADE)
    Doctorado=models.ForeignKey(Doctorado, null=True, blank=True, on_delete = models.CASCADE)

    def __str__(self):
        texto="{1} {2} ({0})"
        return texto.format(self.dni, self.nombre, self.primerApellido)