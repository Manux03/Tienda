from urllib import response
from django.shortcuts import render, redirect
from core.context_processor import retorno_productos
from core.context_processor import total_carrito
from .models import Producto, SubFamilia, Compra
from core.Carrito import Carrito
from django.views.decorators.csrf import csrf_protect
import random
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction


from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout, authenticate
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView

from django.views.generic.edit import FormView #user
from .forms import FormularioLogin, FormularioUsuario, FormularioModifica
from .models import Usuario



# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@csrf_protect
def carrito (request):
    total1 = total_carrito(request)
    retorno = retorno_productos(request)
    if request.method == "POST":
        print(22222222222222)
        return render(request,'core/shopcart.html')
    if total1['total_carrito'] > 0:
        print("Webpay Plus Transaction.create")
        buy_order = str(random.randrange(1000000, 99999999))
        session_id = str(random.randrange(1000000, 99999999))
        total = total_carrito(request)
        amount = total['total_carrito']
        return_url = 'http://127.0.0.1:8000/Pago/'

        response = (Transaction()).create(buy_order, session_id, amount, return_url)

        print(response)
        url=response['url']
        token=response['token']
        contexto= {'url':url,'token':token}
        print(contexto)
        print(retorno['retorno_productos'])
        return render(request,'core/shopcart.html',contexto)

    return render(request,'core/shopcart.html')

def webpay_plus_commit(request):
    token = request.GET.get("token_ws")
    print("commit for token_ws: {}".format(token))

    response = (Transaction()).commit(token=token)
    print("response: {}".format(response))
    idOrden = response['buy_order']
    idUsuario = request.user.idUsuario
    idEstadoCompra = 1
    Compra.objects.create(idOrden = idOrden, idTipopago_id = 1, idUsuario_id = idUsuario, idEstado_id = idEstadoCompra, idSucursal_id = 1 )
    return render(request,'core/shopcart.html')

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
    return render(request, 'core/login2.html')

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
    print (carrito)
    carrito.restar(producto)
    return redirect("Carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Carrito")

#usersssssssss

class Login(FormView):
    template_name = 'core/login2.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('homex')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'core/registro.html'
    success_url = reverse_lazy('homex')

def modifica(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = FormularioUsuario()
        else:
            usuario = Usuario.objects.get(pk=id)
            form = FormularioModifica(instance=usuario)
        return render(request, "core/modifica.html", {'form': form})
    else:
        if id == 0:
            form = FormularioModifica(request.POST)
        else:
            usuario = Usuario.objects.get(pk=id)
            form = FormularioModifica(request.POST,instance= usuario)
        if form.is_valid():
            form.save()
        return redirect('lista')

def eliminar(request,id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect('lista')

def registro(request):
    if request.method == "GET":
        form = FormularioUsuario()
        return render (request,"core/registro.html",{'form':form})
    else:
        form = FormularioUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('core/index.html'))



def lista (request):
    contexto = {'usuarioslista': Usuario.objects.all()}
    return render(request, 'core/listausuarios.html',contexto)


def listausuarios(request):
    datos = {
        'form':FormularioUsuario()
    }
    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    return render(request,'core/listausuarios', datos)
 
    