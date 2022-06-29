from django.contrib import admin
from .models import Producto, Familia, SubFamilia, Region, Provincia, Comuna, Tipo_usuario, Usuario, Sucursal, Estrategia, Estrategia_Detalle, Tipopago, Compra, Estado,Compra_Detalle

# Register your models here.
admin.site.register(Producto)
admin.site.register(Familia)
admin.site.register(SubFamilia)
admin.site.register(Region)
admin.site.register(Provincia)
admin.site.register(Comuna)
admin.site.register(Tipo_usuario)
admin.site.register(Usuario)
admin.site.register(Sucursal)
admin.site.register(Estrategia)
admin.site.register(Estrategia_Detalle)
admin.site.register(Tipopago)
admin.site.register(Compra)
admin.site.register(Estado)
admin.site.register(Compra_Detalle)