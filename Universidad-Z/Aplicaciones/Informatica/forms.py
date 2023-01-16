from django import forms
from .models import *

class Categoriaform(forms.ModelForm):
      class Meta:
          model=Categoria
          fields={
             'idCat',
             'tipoCat',
            }
          labels={
             'idCat':'ID',
             'tipoCat':'Tipo', 
            }
          widgets={
             'idCat':forms.TextInput(attrs={'class':'form-control'}),
             'tipoCat': forms.TextInput(attrs={'class':'form-control'}),
            }

class Contratoform(forms.ModelForm):
      class Meta:
          model=Contrato
          fields={
             'idCont',
             'tipoCont',
            }
          labels={
             'idCont':'ID1',
             'tipoCont':'Tipo1', 
            }
          widgets={
             'idCont':forms.TextInput(attrs={'class':'form-control'}),
             'tipoCont': forms.TextInput(attrs={'class':'form-control'}),
            }

class Maestriaform(forms.ModelForm):
      class Meta:
          model=Maestria
          fields={
             'idMae',
             'tipoMae',
            }
          labels={
             'idMae':'ID2',
             'tipoMae':'Tipo2', 
            }
          widgets={
             'idMAe':forms.TextInput(attrs={'class':'form-control'}),
             'tipoMAe': forms.TextInput(attrs={'class':'form-control'}),
            }

class Doctoradoform(forms.ModelForm):
      class Meta:
          model=Doctorado
          fields={
             'idDoc',
             'tipoDoc',
            }
          labels={
             'idDoc':'ID3',
             'tipoDoc':'Tipo3', 
            }
          widgets={
             'idDoc':forms.TextInput(attrs={'class':'form-control'}),
             'tipoDoc': forms.TextInput(attrs={'class':'form-control'}),
            }

class Profesorform(forms.ModelForm):
      class Meta:
          model=Profesor
          fields={
             'dni',
             'nombre',
             'primerApellido',
             'segundoApellido',
             'sexo',
             'numNomina',
             'fechaIngreso',
             'estado',
             'departamento',
             'Categoria',
             'Contrato',
             'Maestria',
             'Doctorado',
            }
          labels={
             'dni':'ID',
             'nombre':'Nombre',
             'primerApellido':'1er Apellido',
             'segundoApellido':'2do Apellido',
             'sexo':'Sexo',
             'numNomina':'No.Nomina',
             'fechaIngreso':'Año de Ingreso',
             'estado':'Estado',
             'departamento':'Depto',
             'Categoria':'Categoria',
             'Contrato':'Contrato',
             'Maestria':'Maestria',
             'Doctorado':'Doctorado', 
            }
          widgets={
             'dni':forms.TextInput(attrs={'class':'form-control'}),
             'nombre':forms.TextInput(attrs={'class':'form-control'}),
             'primerApellido':forms.TextInput(attrs={'class':'form-control'}),
             'segundoApellido':forms.TextInput(attrs={'class':'form-control'}),
             'sexo':forms.TextInput(attrs={'class':'form-control'}),
             'numNomina':forms.TextInput(attrs={'class':'form-control'}),
             
             'estado':forms.TextInput(attrs={'class':'form-control'}),
             'departamento':forms.TextInput(attrs={'class':'form-control'}),
             'Categoria':forms.Select(attrs={'class':'form-control'}),
             'Contrato':forms.Select(attrs={'class':'form-control'}),
             'Maestria':forms.Select(attrs={'class':'form-control'}),
             'Doctorado':forms.Select(attrs={'class':'form-control'}),
            }            

             