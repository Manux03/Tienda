from django.shortcuts import render, redirect
from .models import Compra, Producto, Familia, SubFamilia, Region, Provincia, Comuna, Sucursal, Tipopago, Estado, Estrategia, Compra_Estado, Compra_Detalle, Estrategia_Detalle
from .forms import ProductoForm,FamiliaForm,SubFamiliaForm, RegionForm, ComunaForm, TipoPagoForm, ProvinciaForm , SucursalForm, EstadoForm, CompraForm, EstrategiaForm, CompraEstadoForm, CompraDetalleForm, EstrategiaDetalleForm

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def adm(request):
    return render(request, 'core/index.html')

def homex(request):
    return render(request, 'core/homex.html')


# Vista de Tablas

def TablaProducto(request):
    contexto = {'productolista': Producto.objects.all()}
    return render(request, 'core/tablaProducto.html', contexto)

def TablaProductoFamilia(request):
    contexto = {'familialista': Familia.objects.all()}
    return render(request, 'core/tablaFamiliaProducto.html', contexto)

def TablaSubFamilia(request):
    contexto = {'subfamilialista': SubFamilia.objects.all()}
    return render(request, 'core/tablaSubFamilia.html', contexto)

def TablaRegion(request):
    contexto = {'regionlista': Region.objects.all()}
    return render(request, 'core/tablaRegion.html', contexto)

def TablaComuna(request):
    contexto = {'comunalista': Comuna.objects.all()}
    return render(request, 'core/tablaComuna.html', contexto)

def TablaCompraEstado(request):
    contexto = {'CompraEstadolista': Compra_Estado.objects.all()}
    return render(request, 'core/tablaCompraEstado.html', contexto)

def TablaEstrategiaDetalle(request):
    contexto = {'EstrategiaDetallelista': Estrategia_Detalle.objects.all()}
    return render(request, 'core/tablaEstrategiaDetalle.html', contexto)

def TablaEstado(request):
    contexto = {'estadolista': Estado.objects.all()}
    return render(request, 'core/tablaEstado.html', contexto)

def TablaProvincia(request):
    contexto = {'provincialista': Provincia.objects.all()}
    return render(request, 'core/tablaProvincia.html', contexto)

def TablaSucursal(request):
    contexto = {'sucursallista': Sucursal.objects.all()}
    return render(request, 'core/tablaSucursal.html', contexto)

def TablaTipoPago(request):
    contexto = {'tipopagolista': Tipopago.objects.all()}
    return render(request, 'core/tablaTipoPago.html', contexto)

def TablaEstrategia(request):
    contexto = {'estrategialista': Estrategia.objects.all()}
    return render(request, 'core/tablaEstrategia.html', contexto)

def TablaCompraDetalle(request):
    contexto = {'compradetallelista': Compra_Detalle.objects.all()}
    return render(request, 'core/tablacompraDetalle.html', contexto)

def TablaCompra(request):
    contexto = {'compralista': Compra.objects.all()}
    return render(request, 'core/tablaCompra.html', contexto)



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

def AgregarComuna(request):
    if request.method == "GET":
        form = ComunaForm()
        return render(request, "core/cComuna.html", {'form': form})
    else:
        form = ComunaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaComuna')

def AgregarSubFamilia(request):
    if request.method == "GET":
        form = SubFamiliaForm()
        return render(request, "core/cSubfamilia.html", {'form': form})
    else:
        form = SubFamiliaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaSubFamilia')

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

def AgregarCompraEstado(request):
    if request.method == "GET":
        form = CompraEstadoForm()
        return render(request, "core/cCompraEstado.html", {'form': form})
    else:
        form = CompraEstadoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaCompraEstado')
        
def AgregarEstrategiaDetalle(request):
    if request.method == "GET":
        form = EstrategiaDetalleForm()
        return render(request, "core/cEstrategiaDetalle.html", {'form': form})
    else:
        form = EstrategiaDetalleForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaEstrategiaDetalle')

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


def AgregarTipoPago(request):
    if request.method == "GET":
        form = TipoPagoForm()
        return render(request, "core/cTipoPago.html", {'form': form})
    else:
        form = TipoPagoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaTipoPago')



def AgregarProducto(request):
    if request.method == "GET":
        form = ProductoForm()
        return render(request, "core/cProducto.html", {'form': form})
    else:
        form = ProductoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaProducto')

def AgregarFamilia(request):
    if request.method == "GET":
        form = FamiliaForm()
        return render(request, "core/cFamilia.html", {'form': form})
    else:
        form = FamiliaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaProductoFamilia')





# Vistas de Modificar (UPDATE)

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
        return redirect('TablaProducto')

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
        return redirect('TablaProductoFamilia')

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
        return redirect('TablaSubFamilia')

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

def ModificaCompraEstado(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = CompraEstadoForm()
        else:
            producto = Compra_Estado.objects.get(pk=id)
            form = CompraEstadoForm(instance= producto)
        return render(request, "core/eCompraEstado.html", {'form': form})
    else:
        if id == 0:
            form = CompraEstadoForm(request.POST)
        else:
            producto = Compra_Estado.objects.get(pk=id)
            form = CompraEstadoForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaCompraEstado')

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

def ModificaEstrategiaDetalle(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EstrategiaDetalleForm()
        else:
            producto = Estrategia_Detalle.objects.get(pk=id)
            form = EstrategiaDetalleForm(instance= producto)
        return render(request, "core/eEstrategiaDetalle.html", {'form': form})
    else:
        if id == 0:
            form = EstrategiaDetalleForm(request.POST)
        else:
            producto = Estrategia_Detalle.objects.get(pk=id)
            form = EstrategiaDetalleForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('tablasEstrategiaDetalle')



# Vistas de Eliminar (DELETE)
def EliminarProducto(request,id):
    producto = Producto.objects.get(pk=id)
    producto.delete()
    return redirect('TablaProducto')

def EliminarFamilia(request,id):
    producto = Familia.objects.get(pk=id)
    producto.delete()
    return redirect('TablaProductoFamilia')

def EliminarRegion(request,id):
    producto = Region.objects.get(pk=id)
    producto.delete()
    return redirect('TablaRegion')

def EliminarProvincia(request,id):
    provincia = Provincia.objects.get(pk=id)
    provincia.delete()
    return redirect('TablaProvincia')

def EliminarComuna(request,id):
    comuna = Comuna.objects.get(pk=id)
    comuna.delete()
    return redirect('TablaComuna')

def EliminarSucursal(request,id):
    sucursal = Sucursal.objects.get(pk=id)
    sucursal.delete()
    return redirect('TablaSucursal')

def EliminarTipopago(request,id):
    tipopago = Tipopago.objects.get(pk=id)
    tipopago.delete()
    return redirect('TablaTipoPago')

def EliminarEstado(request,id):
    estado = Estado.objects.get(pk=id)
    estado.delete()
    return redirect('TablaEstado')

def EliminarCompra(request,id):
    compra = Compra.objects.get(pk=id)
    compra.delete()
    return redirect('TablaCompra')

def EliminarEstrategia(request,id):
    estado = Estrategia.objects.get(pk=id)
    estado.delete()
    return redirect('TablaEstrategia')