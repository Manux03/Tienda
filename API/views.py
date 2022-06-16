from django.views import View
from core.models import Producto, Familia, SubFamilia, Region, Provincia, Comuna, Tipo_usuario, Usuario, Sucursal, Estrategia, Estrategia_Detalle, Tipopago, Compra, Estado,Compra_Detalle
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.
# CRUD API PRODUCTO

class ProductoView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            producto=list(Producto.objects.filter(idProducto=id).values())
            if len(producto) > 0:
                producto = producto[0]
                datos={'message':"Producto existente", 'productos: ': producto }
            else:
                datos={'message':"No hay productos"}   
            return JsonResponse(datos)
        else:
            producto=list(Producto.objects.values())
            if len(producto)>0:
                datos={'message':"Producto existente", 'productos: ': producto }
            else:
                datos={'message':"No hay productos"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Producto.objects.create(idProducto=jd['idProducto'],nombreProducto=jd['nombreProducto'],precio=jd['precio'],stock=jd['stock'],marca=jd['marca'],modelo=jd['modelo'],descripcion=jd['descripcion'],imagen=jd['imagen'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        producto = list(Producto.objects.filter(idProducto=id).values())
        if len (producto) > 0:
            producto = Producto.objects.get (idProducto=id)
            producto.idProducto = jd ['idProducto']
            producto.nombreProducto=jd['nombreProducto']
            producto.precio=jd['precio']
            producto.stock=jd['stock']
            producto.marca=jd['marca']
            producto.modelo=jd['modelo']
            producto.modelo=jd['descripcion']
            producto.modelo=jd['imagen']
            producto.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        producto=list(Producto.objects.filter(idProducto=id).values())
        if len(producto) > 0:
            Producto.objects.filter(idProducto=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay productos"} 

        return JsonResponse(datos)
# FIN CRUD API PRODUCTO




#CRUD API FAMILIA
class FamiliaView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            familia=list(Familia.objects.filter(idFamilia=id).values())
            if len(familia) > 0:
                familia = familia[0]
                datos={'message':"Familia existente", 'familia: ': familia }
            else:
                datos={'message':"No hay familia"}   
            return JsonResponse(datos)
        else:
            familia=list(Familia.objects.values())
            if len(familia)>0:
                datos={'message':"Familia existente", 'familia: ': familia }
            else:
                datos={'message':"No hay familia"}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Familia.create(idFamilia=jd['idFamilia'],nombreFamilia=jd['nombreFamilia'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
        
    def put(self, request, id):
        jd=json.loads(request.body)
        familia = list(Familia.objects.filter(idFamilia=id).values())
        if len (familia) > 0:
            familia = Familia.objects.get (idFamilia=id)
            familia.idFamilia = jd ['idFamilia']
            familia.nombreFamilia=jd['nombreFamilia']
            familia.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        familia=list(Familia.objects.filter(idFamilia=id).values())
        if len(familia) > 0:
            Familia.objects.filter(idFamilia=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay productos"} 

        return JsonResponse(datos)


# FIN CRUD API FAMILIA



# CRUD API SUBFAMILIA
class SubFamiliaView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            subFamilia=list(SubFamilia.objects.filter(idSubFamilia=id).values())
            if len(subFamilia) > 0:
                subFamilia = subFamilia[0]
                datos={'message':"SubFamilia existente", 'subFamilia: ': subFamilia }
            else:
                datos={'message':"No hay SubFamilia"}   
            return JsonResponse(datos)
        else:
            subFamilia=list(SubFamilia.objects.values())
            if len(subFamilia)>0:
                datos={'message':"SubFamilia existente", 'subFamilia: ': subFamilia }
            else:
                datos={'message':"No hay SubFamilia"}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        SubFamilia.objects.create(idSubFamilia=jd['idSubFamilia'],SubFamilia=jd['subFamilia'],producto=jd['producto'],familia=jd['familia'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        subFamilia = list(SubFamilia.objects.filter(idSubFamilia=id).values())
        if len (subFamilia) > 0:
            subFamilia = SubFamilia.objects.get (idSubFamilia=id)
            subFamilia.idSubFamilia = jd ['idSubFamilia']
            subFamilia.SubFamilia=jd['subFamilia']
            subFamilia.producto=jd['producto']
            subFamilia.familia=jd['familia']
            subFamilia.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        subFamilia=list(SubFamilia.objects.filter(idSubFamilia=id).values())
        if len(subFamilia) > 0:
            SubFamilia.objects.filter(idSubFamilia=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay SubFamilia"} 

        return JsonResponse(datos)    

# FIN CRUD API SUBFAMILIA

#CRUD API  REGION
class RegionView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            region=list(Region.objects.filter(idRegion=id).values())
            if len(region) > 0:
                region = region[0]
                datos={'message':"region existente", 'pregion: ': region }
            else:
                datos={'message':"No hay pregion"}   
            return JsonResponse(datos)
        else:
            region=list(Region.objects.values())
            if len(region)>0:
                datos={'message':"region existente", 'pregion: ': region }
            else:
                datos={'message':"No hay pregion"}
            return JsonResponse(datos)
            
    def post(self, request):
        jd=json.loads(request.body)
        Region.objects.create(idRegion=jd['idRegion'],nombre_region=jd['nombre_region'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd=json.loads(request.body)
        region = list(Region.objects.filter(idRegion=id).values())
        if len (region) > 0:
            region = Region.objects.get (idRegion=id)
            region.idRegion = jd ['idRegion']
            region.nombre_region=jd['nombre_region']
            region.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos) 

    def delete(self, request, id):
        region=list(Region.objects.filter(idRegion=id).values())
        if len(region) > 0:
            Region.objects.filter(idRegion=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay region"} 

        return JsonResponse(datos)  
        
# FIN CRUD API REGION



#CRUD API  PROVINCIA
class ProvinciaView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            provincia=list(Provincia.objects.filter(idProvincia=id).values())
            if len(provincia) > 0:
                provincia = provincia[0]
                datos={'message':"provincia existente", 'provincia: ': provincia }
            else:
                datos={'message':"No hay provincia"}   
            return JsonResponse(datos)
        else:
            provincia=list(Provincia.objects.values())
            if len(provincia)>0:
                datos={'message':"Provincia existente", 'provincia: ': provincia }
            else:
                datos={'message':"No hay provincia"}
            return JsonResponse(datos)
    def post(self, request):
        jd=json.loads(request.body)
        Provincia.objects.create(idProvincia=jd['idProvincia'],region_idRegion=jd['region_idRegion'],nombre_provincia=jd['nombre_provincia'])
        datos = {'message': "Success"}
        return JsonResponse(datos)    
    def put(self, request, id):
        jd=json.loads(request.body)
        provincia = list(Provincia.objects.filter(idProvincia=id).values())
        if len (Provincia) > 0:
            provincia = Provincia.objects.get (idProvincia=id)
            provincia.idProvincia = jd ['idRegion']
            provincia.region_idRegion=jd['region_idRegion']
            provincia.nombre_provincia=jd['nombre_provincia']
            provincia.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)     
    def delete(self, request, id):
        provincia=list(Provincia.objects.filter(idProvincia=id).values())
        if len(provincia) > 0:
            Provincia.objects.filter(idProvincia=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay provincia"} 

        return JsonResponse(datos)      
# FIN CRUD API PROVINCIA



#CRUD API  COMUNA
class ComunaView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            comuna=list(Comuna.objects.filter(idComuna=id).values())
            if len(comuna) > 0:
                comuna = comuna[0]
                datos={'message':"provincia existente", 'comuna: ': comuna }
            else:
                datos={'message':"No hay comuna"}   
            return JsonResponse(datos)
        else:
            comuna=list(Comuna.objects.values())
            if len(comuna)>0:
                datos={'message':"Comuna existente", 'comuna: ': comuna }
            else:
                datos={'message':"No hay comuna"}
            return JsonResponse(datos)
    def post(self, request):
        jd=json.loads(request.body)
        Comuna.objects.create(idComuna=jd['idComuna'],Provincia_idProvincia=jd['Provincia_idProvincia'],nombre_comuna=jd['nombre_comuna'])
        datos = {'message': "Success"}
        return JsonResponse(datos)    
    def put(self, request, id):
        jd=json.loads(request.body)
        comuna = list(Comuna.objects.filter(idComuna=id).values())
        if len (Comuna) > 0:
            comuna = Comuna.objects.get (idComuna=id)
            comuna.idComuna = jd ['idRegion']
            comuna.Provincia_idProvincia=jd['Provincia_idProvincia']
            comuna.nombre_comuna=jd['nombre_comuna']
            comuna.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)     
    def delete(self, request, id):
        comuna=list(Comuna.objects.filter(idComuna=id).values())
        if len(comuna) > 0:
            Comuna.objects.filter(idComuna=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay comuna"} 

        return JsonResponse(datos) 
# FIN CRUD API COMUNA



#CRUD API TIPO_USUARIO
class Tipo_usuarioView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            tipo_usuario=list(Tipo_usuario.objects.filter(idTipo_usuario=id).values())
            if len(tipo_usuario) > 0:
                tipo_usuario = tipo_usuario[0]
                datos={'message':"Tipo_usuario existente", 'tipo_usuario: ': tipo_usuario }
            else:
                datos={'message':"No hay tipo_usuario"}   
            return JsonResponse(datos)
        else:
            tipo_usuario=list(Tipo_usuario.objects.values())
            if len(tipo_usuario)>0:
                datos={'message':"Tipo_usuario existente", 'tipo_usuario: ': tipo_usuario }
            else:
                datos={'message':"No hay Tipo_usuario"}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Tipo_usuario.objects.create(idTipo_usuario=jd['idTipo_usuario'],descripcion=jd['descripcion'],descuento=jd['descuento'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
        
    def put(self, request, id):
        jd=json.loads(request.body)
        tipo_usuario = list(Tipo_usuario.objects.filter(idTipo_usuario=id).values())
        if len (tipo_usuario) > 0:
            tipo_usuario = Tipo_usuario.objects.get (idTipo_usuario=id)
            tipo_usuario.idTipo_usuario = jd ['idTipo_usuario']
            tipo_usuario.descripcion=jd['descripcion']
            tipo_usuario.descuento=jd['descuento']
            tipo_usuario.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        tipo_usuario=list(Tipo_usuario.objects.filter(idTipo_usuario=id).values())
        if len(tipo_usuario) > 0:
            Tipo_usuario.objects.filter(idTipo_usuario=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay productos"} 

        return JsonResponse(datos)

# FIN CRUD API TIPO_USUARIO




#CRUD API USUARIO
class UsuarioView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            usuario=list(Usuario.objects.filter(idUsuario=id).values())
            if len(usuario) > 0:
                usuario = usuario[0]
                datos={'message':"Usuario existente", 'usuario: ': usuario }
            else:
                datos={'message':"No hay usuario"}   
            return JsonResponse(datos)
        else:
            usuario=list(Usuario.objects.values())
            if len(usuario)>0:
                datos={'message':"Usuario existente", 'usuario: ': usuario }
            else:
                datos={'message':"No hay Usuario"}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        Usuario.objects.create(idUsuario=jd['idUsuario'],Nombre=jd['Nombre'],Apellido=jd['Apellido'],email=jd['email'],Tipo_usuario_idUsuario=jd['Tipo_usuario_idUsuario'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
        
    def put(self, request, id):
        jd=json.loads(request.body)
        usuario = list(Usuario.objects.filter(idUsuario=id).values())
        if len (usuario) > 0:
            usuario = Usuario.objects.get (idUsuario=id)
            usuario.idUsuario = jd ['idUsuario']
            usuario.Nombre=jd['Nombre']
            usuario.Apellido=jd['Apellido']
            usuario.email=jd['email']
            usuario.Tipo_usuario_idUsuario=jd['Tipo_usuario_idUsuario']
            usuario.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        usuario=list(Usuario.objects.filter(idUsuario=id).values())
        if len(usuario) > 0:
            Usuario.objects.filter(idUsuario=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay usuario"} 

        return JsonResponse(datos)



#CRUD API SUCURSAL
class SucursalView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            sucursal=list(Sucursal.objects.filter(idEstrategia=id).values())
            if len(sucursal) > 0:
                sucursal = sucursal[0]
                datos={'message':"sucursal existente", 'sucursal: ': sucursal }
            else:
                datos={'message':"No hay sucursal"}   
            return JsonResponse(datos)
        else:
            sucursal=list(Sucursal.objects.values())
            if len(sucursal)>0:
                datos={'message':"sucursal existente", 'sucursal: ': sucursal }
            else:
                datos={'message':"No hay sucursal"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Sucursal.objects.create(idSucursal=jd['idSucursal'],sucursal=jd['sucursal'],correo=jd['correo'],telefono=jd['telefono'],idComuna=jd['idComuna'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        sucursal = list(Sucursal.objects.filter(idSucursal=id).values())
        if len (sucursal) > 0:
            sucursal = Sucursal.objects.get (idSucursal=id)
            sucursal.idSucursal = jd ['idSucursal']
            sucursal.sucursal=jd['Sucursal']
            sucursal.correo = jd ['correo']
            sucursal.telefono=jd['telefono']
            sucursal.idComuna = jd ['idComuna']
            sucursal.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        sucursal=list(Sucursal.objects.filter(idSucursal=id).values())
        if len(sucursal) > 0:
            Sucursal.objects.filter(idSucursal=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay sucursal"} 

        return JsonResponse(datos)

#FIN CRUD API SUCURSAL

#CRUD API ESTRATEGIA
class EstrategiaView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            estrategia=list(Estrategia.objects.filter(idEstrategia=id).values())
            if len(estrategia) > 0:
                estrategia = estrategia[0]
                datos={'message':"Estrategia existente", 'estrategia: ': estrategia }
            else:
                datos={'message':"No hay Estrategia"}   
            return JsonResponse(datos)
        else:
            estrategia=list(Estrategia.objects.values())
            if len(estrategia)>0:
                datos={'message':"Estrategia existente", 'estrategia: ': estrategia }
            else:
                datos={'message':"No hay Estrategia"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Estrategia.objects.create(idEstrategia=jd['idEstrategia'],nombreEstrategia=jd['nombreEstrategia'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        estrategia = list(Estrategia.objects.filter(idEstrategia=id).values())
        if len (estrategia) > 0:
            estrategia = Estrategia.objects.get (idEstrategia=id)
            estrategia.idEstrategia = jd ['idEstrategia']
            estrategia.nombreEstrategia=jd['nombreEstrategia']
            estrategia.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        estrategia=list(Estrategia.objects.filter(idEstrategia=id).values())
        if len(estrategia) > 0:
            Estrategia.objects.filter(idEstrategia=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay Estrategia_Detalle"} 

        return JsonResponse(datos)
        
#FIN CRUD ESTRATEGIA


#CRUD API ESTRATEGIA_DETALLE
class Estrategia_DetalleView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            estrategia_detalle=list(Estrategia_Detalle.objects.filter(idEstrategia=id).values())
            if len(estrategia_detalle) > 0:
                estrategia_detalle = estrategia_detalle[0]
                datos={'message':"Estrategia existente", 'estrategia_Detalle: ': estrategia_detalle }
            else:
                datos={'message':"No hay Estrategia"}   
            return JsonResponse(datos)
        else:
            estrategia_detalle=list(Estrategia_Detalle.objects.values())
            if len(estrategia_detalle)>0:
                datos={'message':"Estrategia existente", 'estrategia_Detalle: ': estrategia_detalle }
            else:
                datos={'message':"No hay Estrategia"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Estrategia_Detalle.objects.create(idEstrategia=jd['idEstrategia'],idSucursal=jd['idSucursal'],descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        estrategia_detalle = list(Estrategia_Detalle.objects.filter(idEstrategia=id).values())
        if len (Estrategia_Detalle) > 0:
            estrategia_detalle = Estrategia_Detalle.objects.get (idEstrategia=id)
            estrategia_detalle.idEstrategia_Detalle = jd ['idEstrategia_Detalle']
            estrategia_detalle.idSucursal=jd['idSucursal']
            estrategia_detalle.descripcion=jd['descripcion']
            estrategia_detalle.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        estrategia_detalle=list(Estrategia_Detalle.objects.filter(idEstrategia=id).values())
        if len(estrategia_detalle) > 0:
            Estrategia_Detalle.objects.filter(idEstrategia=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay Estrategia_Detalle"} 

        return JsonResponse(datos)
        
#FIN CRUD ESTRATEGIA DETALLE

#CRUD API TIPO_PAGO
class TipopagoView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            tipopago=list(Tipopago.objects.filter(idTipopago=id).values())
            if len(tipopago) > 0:
                tipopago = tipopago[0]
                datos={'message':"Tipopago existente", 'Tipopago: ': tipopago }
            else:
                datos={'message':"No hay Tipopago"}   
            return JsonResponse(datos)
        else:
            tipopago=list(Tipopago.objects.values())
            if len(tipopago)>0:
                datos={'message':"Tipopago existente", 'Tipopago: ': tipopago }
            else:
                datos={'message':"No hay Tipopago"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Tipopago.objects.create(idTipopago=jd['idTipopago'],tipopago=jd['tipopago'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        tipopago = list(Tipopago.objects.filter(idTipopago=id).values())
        if len (tipopago) > 0:
            tipopago = Tipopago.objects.get (idTipopago=id)
            tipopago.idTipopago = jd ['idTipopago']
            tipopago.tipopago=jd['tipopago']
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        tipopago=list(Tipopago.objects.filter(idTipopago=id).values())
        if len(tipopago) > 0:
            Tipopago.objects.filter(idTipopago=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay Tipopago"} 

        return JsonResponse(datos)

#FIN CRUD API TIPO_PAGO

#CRUD API ESTADO

class EstadoView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            estado=list(Estado.objects.filter(idEstado=id).values())
            if len(estado) > 0:
                estado = estado[0]
                datos={'message':"Estado existente", 'Estado: ': estado }
            else:
                datos={'message':"No hay Estado"}   
            return JsonResponse(datos)
        else:
            estado=list(Estado.objects.values())
            if len(estado)>0:
                datos={'message':"Estado existente", 'productos: ': estado }
            else:
                datos={'message':"No hay Estado"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Estado.objects.create(idEstado=jd['idEstado'],estado=jd['estado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        estado = list(Estado.objects.filter(idEstado=id).values())
        if len (Estado) > 0:
            estado = Estado.objects.get (idEstado=id)
            estado.idEstado = jd ['idPEstado']
            estado.Estado=jd['Estado']
            estado.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        estado=list(Estado.objects.filter(idEstadoo=id).values())
        if len(estado) > 0:
            Estado.objects.filter(idEstado=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay Estado"} 

        return JsonResponse(datos)
#FIN CRUD API ESTADO

#CRUD API COMPRA

class CompraView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            compra=list(Compra.objects.filter(idCompra=id).values())
            if len(compra) > 0:
                compra = compra[0]
                datos={'message':"Compra existente", 'Compra: ': compra }
            else:
                datos={'message':"No hay Compra"}   
            return JsonResponse(datos)
        else:
            compra=list(Compra.objects.values())
            if len(compra)>0:
                datos={'message':"Compra existente", 'Compra: ': compra }
            else:
                datos={'message':"No hay Compra"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Compra.objects.create(idCompra=jd['idCompra'],fechaCompra=jd['fechaCompra'],idTipopago=jd['idTipopago'],idUsuario=jd['idUsuario'],idSucursal=jd['idSucursal'],estado=jd['estado'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        compra = list(Compra.objects.filter(idCompra=id).values())
        if len (Compra) > 0:
            compra = Compra.objects.get (idCompra=id)
            compra.idCompra = jd ['idCompra']
            compra.fechaCompra=jd['fechaCompra']
            compra.idTipopago=jd['idTipopago']
            compra.idUsuario=jd['idUsuario']
            compra.idSucursal=jd['idSucursal']
            compra.estado=jd['estado']
            compra.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        compra=list(Compra.objects.filter(idCompra=id).values())
        if len(compra) > 0:
            Compra.objects.filter(idCompra=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay productos"} 

        return JsonResponse(datos)

#FIN CRUD API COMPRA

#CRUD COMPRA_DETALLE

class Compra_DetalleView(View):
    @method_decorator (csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self, request, id=0):
        if(id>0):
            compra_Detalle=list(Compra_Detalle.objects.filter(idCompra=id).values())
            if len(compra_Detalle) > 0:
                compra_Detalle = compra_Detalle[0]
                datos={'message':"Compra existente", 'Compra: ': compra_Detalle }
            else:
                datos={'message':"No hay Compra"}   
            return JsonResponse(datos)
        else:
            compra_Detalle=list(Compra_Detalle.objects.values())
            if len(compra_Detalle)>0:
                datos={'message':"Compra existente", 'Compra: ': compra_Detalle }
            else:
                datos={'message':"No hay Compra"}
            return JsonResponse(datos)


    def post(self, request):
        jd=json.loads(request.body)
        Compra_Detalle.objects.create(idcompra=jd['idcompra'],idEstado=jd['idEstado'],descripcion=jd['descripcion'])
        datos = {'message': "Success"}
        return JsonResponse(datos)
    
    def put(self, request, id):
        jd=json.loads(request.body)
        compra_Detalle = list(Compra_Detalle.objects.filter(idcompra=id).values())
        if len (compra_Detalle) > 0:
            compra_Detalle = Compra_Detalle.objects.get (idcompra=id)
            compra_Detalle.idcompra = jd ['idcompra']
            compra_Detalle.idEstado=jd['idEstado']
            compra_Detalle.descripcion=jd['descripcion']
            compra_Detalle.save()
            datos={'message':"Modificado Exitosamente"}
        else:
            datos={'message':"Error"}         
        return JsonResponse(datos)

    def delete(self, request, id):
        compra_Detalle=list(Compra_Detalle.objects.filter(idcompra=id).values())
        if len(compra_Detalle) > 0:
            Compra_Detalle.objects.filter(idcompra=id).delete()
            datos={'message':"Eliminado correctamente"}
        else:
            datos={'message':"No hay detalle de compra"} 

        return JsonResponse(datos)
#FIN CRUD API COMPRA_DETALLE