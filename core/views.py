from urllib import response
from django.shortcuts import render, redirect
from .models import Producto, SubFamilia
from core.Carrito import Carrito
from django.views.decorators.csrf import csrf_protect
import requests
import random

from flask import render_template, request
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@csrf_protect
def carrito (request):
    return render(request, 'core/shopcart.html')

def homex(request):
    return render(request, 'core/homex.html')

def create(request):
    return render(request, 'core/create.html')

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


""" def API_TBK_POST(request):
    url = 'http://rswebpaytransaction/api/webpay/v1.2/transactions'
    response = requests.post(url, data = {
                                        "buy_order": "ordenCompra12345678",
                                        "session_id": "sesion1234557545",
                                        "amount": 10000,
                                        "return_url": "http://www.comercio.cl/webpay/retorno"
                                        })
    print(response.json) """

def webpay_plus_create(request):
    print("Webpay Plus Transaction.create")
    buy_order = str(random.randrange(1000000, 99999999))
    session_id = str(random.randrange(1000000, 99999999))
    amount = random.randrange(10000, 1000000)
    return_url = 'http://127.0.0.1:8000/comprar/'

    create_request = {
        "buy_order": buy_order,
        "session_id": session_id,
        "amount": amount,
        "return_url": return_url
    }

    response = (Transaction()).create(buy_order, session_id, amount, return_url)

    print(response)
    url=response['url']
    token=response['token']
    contexto= {'url':url,'token':token}
    print(contexto)
    
    return render(request,'core/shopcart.html',contexto)
    """ return render_template('core/create.html', request=create_request, response=response) """