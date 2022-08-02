
from django.contrib import admin
from django.urls import path

from App_coder.views import familia, lista_dato, inicio
from App_coder.views import base_datos, registro,buscar



urlpatterns = [
    
    path('datos/',lista_dato, name="Datos"),

    path('buscar/',buscar, name="Buscar"),


    path('basededatos/',base_datos, name="inventario"),

     path('registrousuarios/',familia, name="Familia"),


    path('',inicio, name = "inicio"),
    path('registro/',registro, name="Registro"),
    path('agregar_datos/<nombre>/<cargo>/<celular>/<correo>',familia),
]
