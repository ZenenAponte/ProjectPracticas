from django.shortcuts import render
from .models import *
from .forms import *
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home (request):
     return render(request, "home.html")
#Categoria
class CategoriaCreate(CreateView):
     model=Categoria
     form_class=Categoriaform
     template_name='home.html'
     success_url=reverse_lazy('CrearCategoria')

class CategoriaList(ListView):
      model=Categoria
      template_name='home.html'

class CategoriaUpdate(UpdateView):
      model=Categoria
      form_class=Categoriaform
      template_name='home.html'
      success_url=reverse_lazy('UpdateCategoria')

class CategoriaDelete(DeleteView):
      model=Categoria
      form_class=Categoriaform
      template_name='home.html'
      success_url=reverse_lazy('DeleteCategoria')


#Contrato
class ContratoCreate(CreateView):
     model=Contrato
     form_class=Contratoform
     template_name='home.html'
     success_url=reverse_lazy('CrearContrato')

class ContratoList(ListView):
      model=Contrato
      template_name='home.html'

class ContratoUpdate(UpdateView):
      model=Contrato
      form_class=Contratoform
      template_name='home.html'
      success_url=reverse_lazy('UpdateContrato')

class ContratoDelete(DeleteView):
      model=Contrato
      form_class=Contratoform
      template_name='home.html'
      success_url=reverse_lazy('DeleteContrato')     



#Maestria
class MaestriaCreate(CreateView):
     model=Maestria
     form_class=Maestriaform
     template_name='home.html'
     success_url=reverse_lazy('CrearMaestria')

class MaestriaList(ListView):
      model=Maestria
      template_name='home.html'

class MaestriaUpdate(UpdateView):
      model=Maestria
      form_class=Maestriaform
      template_name='home.html'
      success_url=reverse_lazy('UpdateMaestria')

class MaestriaDelete(DeleteView):
      model=Maestria
      form_class=Maestriaform
      template_name='home.html'
      success_url=reverse_lazy('DeleteMaestria')     


#Doctorado
class DoctoradoCreate(CreateView):
     model=Doctorado
     form_class=Doctoradoform
     template_name='home.html'
     success_url=reverse_lazy('CrearDoctorado')

class DoctoradoList(ListView):
      model=Doctorado
      template_name='home.html'

class DoctoradoUpdate(UpdateView):
      model=Doctorado
      form_class=Doctoradoform
      template_name='home.html'
      success_url=reverse_lazy('UpdateDoctorado')

class DoctoradoDelete(DeleteView):
      model=Doctorado
      form_class=Doctoradoform
      template_name='home.html'
      success_url=reverse_lazy('DeleteDoctorado')     


#Profesor
class ProfesorCreate(CreateView):
     model=Profesor
     form_class=Profesorform
     template_name='home.html'
     success_url=reverse_lazy('CrearProfesor')

class ProfesorList(ListView):
      model=Profesor
      template_name='home.html'

class ProfesorUpdate(UpdateView):
      model=Profesor
      form_class=Profesorform
      template_name='home.html'
      success_url=reverse_lazy('UpdateProfesor')

class ProfesorDelete(DeleteView):
      model=Profesor
      form_class=Profesorform
      template_name='home.html'
      success_url=reverse_lazy('DeleteProfesor') 