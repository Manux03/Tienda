from django.urls import path
from .views import Tienda, agregar_producto, carrito, create, eliminar_producto, home, homex, ProductoDetalle, login, limpiar_carrito, restar_producto, webpay_plus_commit
from .views import Login, logoutUsuario,RegistrarUsuario, lista, modifica,eliminar #user
from django.contrib.auth.decorators import login_required #user
from django.conf import settings #user
from django.conf.urls.static import static #user

urlpatterns = [
    path('home/', home, name='home'),
    path('homex/', homex, name='homex'),
    path('Tienda/', Tienda, name='Tienda'),
    path('Carrito/', carrito, name="Carrito"),
    path('Tienda/Producto/<int:id>/', ProductoDetalle,name='ProductoDetalle'), 
    path('accounts/login/',Login.as_view(), name = 'login'),
    path('agregar/<int:id>/', agregar_producto, name="Add"),
    path('eliminar/<int:id>/', eliminar_producto, name="Del"),
    path('restar/<int:id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('create/', create, name="create"),
    path('logout/',login_required(logoutUsuario),name = 'logout'),
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registro'),
    path('Pago/',webpay_plus_commit,name = 'pago')
]