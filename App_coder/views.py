from doctest import ELLIPSIS_MARKER
from unittest.result import failfast
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from App_coder.models import mifamilia
from .forms import inventario, puntoventa, registrousuarios
from .models import ferreteria, ventas

# Create your views here.
def familia(request):

    if request.method == "POST":
    
        familia = registrousuarios(request.POST)

        if familia.is_valid():

            info =familia.cleaned_data

            usuarios = mifamilia(nombre=info['nombre'], cargo=info['cargo'], celular=info['celular'], correo=info['correo'])

            usuarios.save()

            return redirect("inicio")

        return render(request, 'registrousuarios.html')
    else:

        familia = registrousuarios()
         

    return render(request, "registrousuarios.html", {"familia": familia})



def lista_dato(request):

      return render(request, "lista_datos.html")

def buscar(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]

        productos = ferreteria.objects.filter(nombre_elemen__icontains=nombre)


        return render(request, "resultadobusqueda.html", {"productos":productos, "referencia": nombre })

    else:

        respuesta = "No escribiste datos"


    return HttpResponse(respuesta)









def inicio(self):

    return render(self, "inicio.html")


def base_datos(request):

    if request.method == "POST":

        miformulario = inventario(request.POST)

        if miformulario.is_valid():

            data = miformulario.cleaned_data

            Ferreteria = ferreteria(nombre_elemen=data['nombre_elemen'], referencia=data['referencia'], cantidad=data['cantidad'], precio_uni=data['precio_uni'], precio_cos=data['precio_cos'])
        
            Ferreteria.save()

            return redirect("inicio")

        return render(request, 'base_datos.html')
    else:

        miformulario = inventario()


    return render(request, "base_datos.html", {"miformulario": miformulario})

def registro(request):

    if request.method == "POST":

        ventaspro = puntoventa(request.POST)

        if ventaspro.is_valid():

            valor = ventaspro.cleaned_data

            guardar = ventas(nombre_element=valor['nombre_element'], referencia_pro=valor['referencia_pro'], cantidad_ven=valor['cantidad_ven'], precio=valor['precio'])
            guardar.save()

            return redirect("inicio")

        return render(request, 'registro.html')
    else:

        ventaspro = puntoventa()

    return render(request, "registro.html", {"ventaspro": ventaspro})




 

