from django.urls import path
from .views import Tienda, agregar_producto, carrito, eliminar_producto, home, homex, ProductoDetalle, Login, limpiar_carrito, restar_producto

urlpatterns = [
    path('home/', home, name='home'),
    path('homex/', homex, name='homex'),
    path('Tienda/', Tienda, name='Tienda'),
    path('Carrito/', carrito, name="Carrito"),
    path('Tienda/Producto/<int:id>/', ProductoDetalle,name='ProductoDetalle'), 
    path('Login/', Login, name='Login'),
    path('agregar/<int:id>/', agregar_producto, name="Add"),
    path('eliminar/<int:id>/', eliminar_producto, name="Del"),
    path('restar/<int:id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]