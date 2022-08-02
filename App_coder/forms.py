from django import forms


class inventario(forms.Form):

    nombre_elemen = forms.CharField()
    referencia = forms.CharField()
    cantidad = forms.IntegerField()
    precio_uni = forms.IntegerField()
    precio_cos = forms.IntegerField()

class puntoventa(forms.Form):

    nombre_element =  forms.CharField()
    referencia_pro = forms.CharField()
    cantidad_ven = forms.IntegerField()
    precio = forms.IntegerField()

class registrousuarios(forms.Form):

    nombre = forms.CharField()
    cargo = forms.CharField()
    celular = forms.IntegerField()
    correo = forms.EmailField()