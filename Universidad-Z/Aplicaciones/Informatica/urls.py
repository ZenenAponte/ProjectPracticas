from django.urls import path
from . import views

urlpatterns = [
    path('', views.CategoriaCreate.as_view(),name='CrearCategoria')
]
urlpatterns = [
    path('', views.ContratoCreate.as_view(),name='CrearContrato')
]
urlpatterns = [
    path('', views.MaestriaCreate.as_view(),name='CrearMaestria')
]
urlpatterns = [
    path('', views.DoctoradoCreate.as_view(),name='CrearDoctorado')
]
urlpatterns = [
    path('', views.ProfesorCreate.as_view(),name='CrearProfesor')
]