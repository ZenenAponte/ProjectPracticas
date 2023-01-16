from django import forms
from .models import *

class MapaConceptualform(forms.ModelForm):
    class Meta:
        model=MapaConceptual
        fields={
            'codigo',
            'nombre',
        }
        labels={
            'codigo':'Codigo',
            'nombre':'Nombre',
        }
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
        }

class Nodoform(forms.ModelForm):
    class Meta:
        model=Nodo
        fields={
            'codigo',
            'nombre',
        }
        labels={
            'codigo':'Codigo',
            'nombre':'Nombre',
        }
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'MapaConseptual':forms.Select(attrs={'class':'form-control'})
        }

class Evaluacionform(forms.ModelForm):
    class Meta:
        model=Evaluacion
        fields={
           'codigo',
           'nombre',
           'puntuacion_minima',
        }
        labels={
           'codigo':'Codigo',
           'nombre':'Nombre',
           'puntuacion_minima':'Puntuacion Minima',
        }
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'puntuacion_minima':forms.TextInput(attrs={'class':'form-control'}),
        }

class Ejercicioform(forms.ModelForm):
    class Meta:
        model=Ejercicio
        fields={
            'codigo',
            'nombre',
        }
        labels={
            'codigo':'Codigo',
            'nombre':'Nombre',
        }
        widgets={
            'codigo':forms.TextInput(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'Nodo':forms.Select(attrs={'class':'form-control'}),
            'Evaluacion':forms.Select(attrs={'class':'form-control'}),

        }
        


        
    