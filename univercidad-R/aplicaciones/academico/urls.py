from django.urls import path
from . import views

urlpatterns=[
    path('', views.MapaConceptualCreate.as_view(),name='GestionarMapa'),
    path('', views.MapaConceptualCreate.as_view(),name='GestionarNodo'),
    path('', views.MapaConceptualCreate.as_view(),name='GestionarEvaluacion'),
    path('', views.MapaConceptualCreate.as_view(),name='GestionarEjercicio')
    
]