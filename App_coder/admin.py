from django.contrib import admin

from .models import ferreteria, mifamilia, ventas

class ferreteriaAdmin(admin.ModelAdmin):
    
    list_display = ["nombre_elemen", "referencia", "cantidad", "precio_uni", "precio_cos"]
    search_fields = ["nombre_elemen", "referencia"]

class ventasAdmin(admin.ModelAdmin):
    
    list_display = ["nombre_element", "referencia_pro", "cantidad_ven", "precio"]
    search_fields = ["nombre_element", "referencia_pro"]

class mifamiliaAdmin(admin.ModelAdmin):
    
    list_display = ["nombre", "cargo", "celular", "correo"]
    search_fields = ["nombre",]

# Register your models here.
admin.site.register(ferreteria, ferreteriaAdmin) 
admin.site.register(mifamilia, mifamiliaAdmin)
admin.site.register(ventas, ventasAdmin)