from django.shortcuts import render, redirect
from .models import Producto, SubFamilia
from core.Carrito import Carrito
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def carrito (request):
    return render(request, 'core/shopcart.html')

def homex(request):
    return render(request, 'core/homex.html')

def Tienda (request):
    contexto = {'productolista': Producto.objects.all()}
    return render (request,'core/tiendalista.html', contexto)

def ProductoDetalle (request, id):
    contexto = {'productodetalle': SubFamilia.objects.select_related('producto','familia').get(producto = id)}
    print (contexto)
    return render (request,'core/detalleProducto.html', contexto)

def Login(request):
    return render(request, 'core/Login.html')

def agregar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.agregar(producto)
    return redirect("Carrito")

def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.eliminar(producto)
    return redirect("Carrito")

def restar_producto(request,id):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito.restar(producto)
    return redirect("Carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Carrito")