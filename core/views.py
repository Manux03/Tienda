from django.shortcuts import render
from django.views import View
from .models import Producto
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
def home(request):
    return render(request, 'core/home.html')
    

    
class ProductoView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            producto=list(Producto.objects.filter(idProducto=id).values())
            if len(producto) > 0:
                producto = producto[0]
                datos={'message':"Exito", 'usuarios: ': producto }
            else:
                datos={'message':"No hay usuarios"}   
            return JsonResponse(datos)
        else:
            producto=list(Producto.objects.values())
            if len(producto)>0:
                datos={'message':"Exito", 'usuarios: ': producto }
            else:
                datos={'message':"No hay usuarios"}   
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Producto.objects.create(idProducto=jd['idProducto'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        producto = list(Producto.objects.filter(idProducto=id).values())
        if len (producto) > 0:
            producto = Producto.objects.get (idProducto=id)
            producto.idProducto = jd ['idProducto']
            producto.save()
            datos={'message':"Exito"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        producto=list(Producto.objects.filter(idProducto=id).values())
        if len(producto) > 0:
            Producto.objects.filter(idProducto=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay usuarios"} 

        return JsonResponse(datos)