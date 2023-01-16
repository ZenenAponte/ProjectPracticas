from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    MapaConceptuales=MapaConceptual.objects.all()
    return render(request, "GestionMapaConseptual.html",{"mapaconceptual":MapaConceptuales})

class MapaConceptualCreate(CreateView):
    model=MapaConceptual
    form_class=MapaConceptualform
    template_name='GestionMapaConseptual.html'
    success_url= reverse_lazy('GestionarMapa')

class MapaConceptualList(ListView):
    model=MapaConceptual
    template_name='GestionMapaConseptual.html'

class MapaConceptualUpdate(UpdateView):
    model=MapaConceptual
    form_class=MapaConceptualform
    template_name='GestionMapaConseptual.html'
    success_url= reverse_lazy('GestionarMapa')

class MapaConceptualDelete(DeleteView):
    model=MapaConceptual
    form_class=MapaConceptualform
    template_name='GestionMapaConseptual.html'
    success_url= reverse_lazy('GestionarMapa')

class NodoCreate(CreateView):
    model=Nodo
    form_class=Nodoform
    template_name='GestionarNodo.html'
    success_url= reverse_lazy('GestionarNodo')

class NodoList(ListView):
    model=Nodo
    template_name='GestionarNodo.html'

class NodoUpdate(UpdateView):
    model=Nodo
    form_class=Nodoform
    template_name='GestionarNodo.html'
    success_url= reverse_lazy('GestionarNodo')

class NodoDelete(DeleteView):
    model=Nodo
    form_class=Nodoform
    template_name='GestionarNodo.html'
    success_url= reverse_lazy('GestionarNodo')

class EvaluacionCreate(CreateView):
    model=Evaluacion
    form_class=Evaluacionform
    template_name='GestionarEvaluacion.html'
    success_url= reverse_lazy('GestionarEvaluacion')

class EvaluacionList(ListView):
    model=Evaluacion
    template_name='GestionarEvaluacion.html'

class EvaluacionUpdate(UpdateView):
    model=Evaluacion
    form_class=Evaluacionform
    template_name='GestionarEvaluacion.html'
    success_url= reverse_lazy('GestionarEvaluacion')

class EvaluacionDelete(DeleteView):
    model=Evaluacion
    form_class=Evaluacionform
    template_name='GestionarEvaluacion.html'
    success_url= reverse_lazy('GestionarEvaluacion')

class EjercicioCreate(CreateView):
    model=Ejercicio
    form_class=Ejercicioform
    template_name='GestionarEjercicio.html'
    success_url= reverse_lazy('GestionarEjercicio')

class EjercicioList(ListView):
    model=Ejercicio
    template_name='GestionarEjercicio.html'

class EjercicioUpdate(UpdateView):
    model=Ejercicio
    form_class=Ejercicioform
    template_name='GestionarEjercicio.html'
    success_url= reverse_lazy('EjercicioEvaluacion')

class EjercicioDelete(DeleteView):
    model=Ejercicio
    form_class=Ejercicioform
    template_name='GestionarEjercicio.html'
    success_url= reverse_lazy('GestionarEjercicio')