from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from .models import Compra, Producto, Familia, SubFamilia, Region, Provincia, Comuna, Sucursal, Tipopago, Estado, Estrategia, Compra_Estado, Compra_Detalle, Estrategia_Detalle
from .forms import ProductoForm,FamiliaForm,SubFamiliaForm, RegionForm, ComunaForm, TipoPagoForm, ProvinciaForm , SucursalForm, EstadoForm, CompraForm, EstrategiaForm, Compra_EstadoForm, CompraDetalleForm, Estrategia_DetalleForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def adm(request):
    return render(request, 'core/index.html')

def homex(request):
    return render(request, 'core/homex.html')



# Vista de Tablas



def tables(request):
    contexto = {'usuarioslista': Producto.objects.all()}
    return render(request, 'core/tables.html', contexto)

def Tabla_Producto_Familia(request):
    contexto = {'familialista': Familia.objects.all()}
    return render(request, 'core/tablafamiliaproducto.html', contexto)

def Tabla_Sub_Familia(request):
    contexto = {'subfamilialista': SubFamilia.objects.all()}
    return render(request, 'core/tablasubfamilia.html', contexto)

def Tabla_Region(request):
    contexto = {'regionlista': Region.objects.all()}
    return render(request, 'core/tablaregion.html', contexto)

def TablaComuna(request):
    contexto = {'comunalista': Comuna.objects.all()}
    return render(request, 'core/tablacomuna.html', contexto)

def TablaCompra_Estado(request):
    contexto = {'Compra_Estadolista': Compra_Estado.objects.all()}
    return render(request, 'core/tablaCompra_Estado.html', contexto)

def TablaEstrategia_Detalle(request):
    contexto = {'Estrategia_Detallelista': Estrategia_Detalle.objects.all()}
    return render(request, 'core/tablaEstrategia_Detalle.html', contexto)

def TablaEstado(request):
    contexto = {'estadolista': Estado.objects.all()}
    return render(request, 'core/tablaestado.html', contexto)

def TablaProvincia(request):
    contexto = {'provincialista': Provincia.objects.all()}
    return render(request, 'core/tablaprovincia.html', contexto)

def TablaSucursal(request):
    contexto = {'sucursallista': Sucursal.objects.all()}
    return render(request, 'core/tablasucursal.html', contexto)

def TablaTipoPago(request):
    contexto = {'tipopagolista': Tipopago.objects.all()}
    return render(request, 'core/tablatipopago.html', contexto)

def TablaEstrategia(request):
    contexto = {'estrategialista': Estrategia.objects.all()}
    return render(request, 'core/tablaestrategia.html', contexto)

def TablaCompraDetalle(request):
    contexto = {'compradetallelista': Compra_Detalle.objects.all()}
    return render(request, 'core/tablacompradetalle.html', contexto)





# Vistas de Agregar (ADD)

def AgregarEstrategia(request):
    if request.method == "GET":
        form = EstrategiaForm()
        return render(request, "core/cEstrategia.html", {'form': form})
    else:
        form = EstrategiaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaEstrategia')

def EliminarEstrategia(request,id):
    estado = Estrategia.objects.get(pk=id)
    estado.delete()
    return redirect('TablaEstrategia')

def ModificaEstrategia(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EstrategiaForm()
        else:
            producto = Estrategia.objects.get(pk=id)
            form = EstrategiaForm(instance= producto)
        return render(request, "core/eEstrategia.html", {'form': form})
    else:
        if id == 0:
            form = EstrategiaForm(request.POST)
        else:
            producto = Estrategia.objects.get(pk=id)
            form = EstrategiaForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaEstrategia')

def TablaCompra(request):
    contexto = {'compralista': Compra.objects.all()}
    return render(request, 'core/tablacompra.html', contexto)

def AgregarComuna(request):
    if request.method == "GET":
        form = ComunaForm()
        return render(request, "core/cComuna.html", {'form': form})
    else:
        form = ComunaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaComuna')

def EliminarComuna(request,id):
    comuna = Comuna.objects.get(pk=id)
    comuna.delete()
    return redirect('TablaComuna')

def EliminarEstado(request,id):
    estado = Estado.objects.get(pk=id)
    estado.delete()
    return redirect('TablaEstado')


def ModificaComuna(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ComunaForm()
        else:
            producto = Comuna.objects.get(pk=id)
            form = ComunaForm(instance= producto)
        return render(request, "core/eComuna.html", {'form': form})
    else:
        if id == 0:
            form = ComunaForm(request.POST)
        else:
            producto = Comuna.objects.get(pk=id)
            form = ComunaForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaComuna')

def ModificaEstado(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EstadoForm()
        else:
            producto = Estado.objects.get(pk=id)
            form = EstadoForm(instance= producto)
        return render(request, "core/eEstado.html", {'form': form})
    else:
        if id == 0:
            form = EstadoForm(request.POST)
        else:
            producto = Estado.objects.get(pk=id)
            form = EstadoForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaEstado')

def ModificaSucursal(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = SucursalForm()
        else:
            producto = Sucursal.objects.get(pk=id)
            form = SucursalForm(instance= producto)
        return render(request, "core/eSucursal.html", {'form': form})
    else:
        if id == 0:
            form = SucursalForm(request.POST)
        else:
            producto = Sucursal.objects.get(pk=id)
            form = SucursalForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaSucursal')

def AgregarSubFamilia(request):
    if request.method == "GET":
        form = SubFamiliaForm()
        return render(request, "core/cSubfamilia.html", {'form': form})
    else:
        form = SubFamiliaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('tablasubfamilia')

def AgregarCompraDetalle(request):
    if request.method == "GET":
        form = CompraDetalleForm()
        return render(request, "core/cCompraDetalle.html", {'form': form})
    else:
        form = CompraDetalleForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaCompraDetalle')
        
def AgregarRegion(request):
    if request.method == "GET":
        form = RegionForm()
        return render(request, "core/cRegion.html", {'form': form})
    else:
        form = RegionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaRegion')

def AgregarCompra_Estado(request):
    if request.method == "GET":
        form = Compra_EstadoForm()
        return render(request, "core/cCompra_Estado.html", {'form': form})
    else:
        form = Compra_EstadoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaCompra_Estado')

def AgregarEstrategia_Detalle(request):
    if request.method == "GET":
        form = Estrategia_DetalleForm()
        return render(request, "core/cEstrategia_Detalle.html", {'form': form})
    else:
        form = Estrategia_DetalleForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaEstrategia_Detalle')

def AgregarEstado(request):
    if request.method == "GET":
        form = EstadoForm()
        return render(request, "core/cEstado.html", {'form': form})
    else:
        form = EstadoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaEstado')

def AgregarSucursal(request):
    if request.method == "GET":
        form = SucursalForm()
        return render(request, "core/cSucursal.html", {'form': form})
    else:
        form = SucursalForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaSucursal')

def AgregarProvincia(request):
    if request.method == "GET":
        form = ProvinciaForm()
        return render(request, "core/cProvincia.html", {'form': form})
    else:
        form = ProvinciaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaProvincia')


def AgregarCompra(request):
    if request.method == "GET":
        form = CompraForm()
        return render(request, "core/cCompra.html", {'form': form})
    else:
        form = CompraForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaCompra')


def EliminarProvincia(request,id):
    provincia = Provincia.objects.get(pk=id)
    provincia.delete()
    return redirect('TablaProvincia')

def ModificaProvincia(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProvinciaForm()
        else:
            producto = Provincia.objects.get(pk=id)
            form = ProvinciaForm(instance= producto)
        return render(request, "core/eProvincia.html", {'form': form})
    else:
        if id == 0:
            form = ProvinciaForm(request.POST)
        else:
            producto = Provincia.objects.get(pk=id)
            form = ProvinciaForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaProvincia')

def AgregarTipoPago(request):
    if request.method == "GET":
        form = TipoPagoForm()
        return render(request, "core/cTipoPago.html", {'form': form})
    else:
        form = TipoPagoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaTipoPago')

def EliminarRegion(request,id):
    producto = Region.objects.get(pk=id)
    producto.delete()
    return redirect('TablaRegion')

def ModificaRegion(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = RegionForm()
        else:
            producto = Region.objects.get(pk=id)
            form = RegionForm(instance= producto)
        return render(request, "core/eRegion.html", {'form': form})
    else:
        if id == 0:
            form = RegionForm(request.POST)
        else:
            producto = Region.objects.get(pk=id)
            form = RegionForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaRegion')



def ModificaSubFamilia(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = SubFamiliaForm()
        else:
            producto = SubFamilia.objects.get(pk=id)
            form = SubFamiliaForm(instance= producto)
        return render(request, "core/eSubfamilia.html", {'form': form})
    else:
        if id == 0:
            form = SubFamilia(request.POST)
        else:
            producto = SubFamilia.objects.get(pk=id)
            form = SubFamiliaForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('tablasubfamilia')

def ModificaCompraDetalle(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = CompraDetalleForm()
        else:
            idcompra = Compra_Detalle.objects.get(pk=id)
            form = CompraDetalleForm(instance= idcompra)
        return render(request, "core/eCompraDetalle.html", {'form': form})
    else:
        if id == 0:
            form = CompraDetalleForm(request.POST)
        else:
            idcompra = Compra_Detalle.objects.get(pk=id)
            form = CompraDetalleForm(request.POST or None,request.FILES or None, instance = idcompra)
        if form.is_valid():
            form.save()
        return redirect('TablaCompraDetalle')

def eliminars(request,id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return redirect('tables')

def ModificaProducto(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductoForm()
        else:
            producto = Producto.objects.get(pk=id)
            form = ProductoForm(instance= producto)
        return render(request, "core/eProducto.html", {'form': form})
    else:
        if id == 0:
            form = ProductoForm(request.POST)
        else:
            producto = Producto.objects.get(pk=id)
            form = ProductoForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('tables')

def ModificaCompra_Estado(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Compra_EstadoForm()
        else:
            producto = Compra_Estado.objects.get(pk=id)
            form = Compra_EstadoForm(instance= producto)
        return render(request, "core/eCompra_Estado.html", {'form': form})
    else:
        if id == 0:
            form = Compra_EstadoForm(request.POST)
        else:
            producto = Compra_Estado.objects.get(pk=id)
            form = Compra_EstadoForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('tablasCompra_Estado')

def ModificaEstrategia_Detalle(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = Estrategia_DetalleForm()
        else:
            producto = Estrategia_Detalle.objects.get(pk=id)
            form = Estrategia_DetalleForm(instance= producto)
        return render(request, "core/eEstrategia_Detalle.html", {'form': form})
    else:
        if id == 0:
            form = Estrategia_DetalleForm(request.POST)
        else:
            producto = Estrategia_Detalle.objects.get(pk=id)
            form = Estrategia_DetalleForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('tablasEstrategia_Detalle')

def AgregarProducto(request):
    if request.method == "GET":
        form = ProductoForm()
        return render(request, "core/cProducto.html", {'form': form})
    else:
        form = ProductoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('tables')

def AgregarFamilia(request):
    if request.method == "GET":
        form = FamiliaForm()
        return render(request, "core/cFamilia.html", {'form': form})
    else:
        form = FamiliaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('tablafamilia')





# Vistas de Modificar (UPDATE)






def ModificaFamilia(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = FamiliaForm()
        else:
            producto = Familia.objects.get(pk=id)
            form = FamiliaForm(instance= producto)
        return render(request, "core/eFamilia.html", {'form': form})
    else:
        if id == 0:
            form = Familia(request.POST)
        else:
            producto = Familia.objects.get(pk=id)
            form = FamiliaForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('tablafamilia')

def ModificaTipoPago(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = TipoPagoForm()
        else:
            tipopago = Tipopago.objects.get(pk=id)
            form = TipoPagoForm(instance= tipopago)
        return render(request, "core/eTipoPago.html", {'form': form})
    else:
        if id == 0:
            form = Tipopago(request.POST)
        else:
            tipopago = Tipopago.objects.get(pk=id)
            form = TipoPagoForm(request.POST or None,request.FILES or None, instance = tipopago)
        if form.is_valid():
            form.save()
        return redirect('TablaTipoPago')

def ModificaCompra(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = CompraForm()
        else:
            producto = Compra.objects.get(pk=id)
            form = CompraForm(instance= producto)
        return render(request, "core/eCompra.html", {'form': form})
    else:
        if id == 0:
            form = CompraForm(request.POST)
        else:
            producto = Compra.objects.get(pk=id)
            form = CompraForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaCompra')






# Vistas de Eliminar (DELETE)


def EliminarFamilia(request,id):
    producto = Familia.objects.get(pk=id)
    producto.delete()
    return redirect('tablafamilia')

def EliminarTipopago(request,id):
    tipopago = Tipopago.objects.get(pk=id)
    tipopago.delete()
    return redirect('TablaTipoPago')

def EliminarSucursal(request,id):
    sucursal = Sucursal.objects.get(pk=id)
    sucursal.delete()
    return redirect('TablaSucursal')

def EliminarCompra(request,id):
    compra = Compra.objects.get(pk=id)
    compra.delete()
    return redirect('TablaComuna')

