from django.shortcuts import render, redirect
from core.models import Compra, Producto, Familia, SubFamilia, Region, Provincia, Comuna, Sucursal, Tipopago, Estado, Estrategia, Compra_Detalle, Estrategia_Detalle
from .forms import ProductoForm,FamiliaForm,SubFamiliaForm, RegionForm, ComunaForm, TipoPagoForm, ProvinciaForm , SucursalForm, EstadoForm, CompraForm, EstrategiaForm, CompraDetalleForm, EstrategiaDetalleForm

# Create your views here.
def adm(request):
    return render(request, 'index.html')

# Vista de Tablas

def TablaProducto(request):
    contexto = {'productolista': Producto.objects.all()}
    return render(request, 'tablaProducto.html', contexto)

def TablaProductoFamilia(request):
    contexto = {'familialista': Familia.objects.all()}
    return render(request, 'tablaFamiliaProducto.html', contexto)

def TablaSubFamilia(request):
    contexto = {'subfamilialista': SubFamilia.objects.all()}
    return render(request, 'tablaSubFamilia.html', contexto)

def TablaRegion(request):
    contexto = {'regionlista': Region.objects.all()}
    return render(request, 'tablaRegion.html', contexto)

def TablaProvincia(request):
    contexto = {'provincialista': Provincia.objects.select_related('region_idRegion').all()}
    return render(request, 'tablaProvincia.html', contexto)

def TablaComuna(request):
    contexto = {'comunalista': Comuna.objects.select_related('Provincia_idProvincia').all()}
    return render(request, 'tablaComuna.html', contexto)

def TablaSucursal(request):
    contexto = {'sucursallista': Sucursal.objects.select_related('idComuna').all()}
    return render(request, 'tablaSucursal.html', contexto)

def TablaTipoPago(request):
    contexto = {'tipopagolista': Tipopago.objects.all()}
    return render(request, 'tablaTipoPago.html', contexto)

def TablaEstado(request):
    contexto = {'estadolista': Estado.objects.all()}
    return render(request, 'tablaEstado.html', contexto)
   
def TablaCompraDetalle(request):
    contexto = {'compradetallelista': Compra_Detalle.objects.select_related('idOrden', 'idProducto').all()}
    return render(request, 'tablacompraDetalle.html', contexto)

def TablaCompra(request):
    contexto = {'compralista': Compra.objects.select_related('idTipopago', 'idUsuario', 'idSucursal').all()}
    return render(request, 'tablaCompra.html', contexto)

def TablaEstrategia(request):
    contexto = {'estrategialista': Estrategia.objects.all()}
    return render(request, 'tablaEstrategia.html', contexto)

def TablaEstrategiaDetalle(request):
    contexto = {'EstrategiaDetallelista': Estrategia_Detalle.objects.all()}
    return render(request, 'tablaEstrategiaDetalle.html', contexto)

# Vistas de Agregar (ADD)

def AgregarProducto(request):
    if request.method == "GET":
        form = ProductoForm()
        return render(request, "cProducto.html", {'form': form})
    else:
        form = ProductoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaProducto')

def AgregarFamilia(request):
    if request.method == "GET":
        form = FamiliaForm()
        return render(request, "cFamilia.html", {'form': form})
    else:
        form = FamiliaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaProductoFamilia')

def AgregarSubFamilia(request):
    if request.method == "GET":
        form = SubFamiliaForm()
        return render(request, "cSubfamilia.html", {'form': form})
    else:
        form = SubFamiliaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaSubFamilia')

def AgregarRegion(request):
    if request.method == "GET":
        form = RegionForm()
        return render(request, "cRegion.html", {'form': form})
    else:
        form = RegionForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaRegion')
def AgregarProvincia(request):
    if request.method == "GET":
        form = ProvinciaForm()
        return render(request, "cProvincia.html", {'form': form})
    else:
        form = ProvinciaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaProvincia')
def AgregarComuna(request):
    if request.method == "GET":
        form = ComunaForm()
        return render(request, "cComuna.html", {'form': form})
    else:
        form = ComunaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaComuna')        
def AgregarSucursal(request):
    if request.method == "GET":
        form = SucursalForm()
        return render(request, 'cSucursal.html', {'form': form})
    else:
        form = SucursalForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaSucursal')
def AgregarTipoPago(request):
    if request.method == "GET":
        form = TipoPagoForm()
        return render(request, "cTipoPago.html", {'form': form})
    else:
        form = TipoPagoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaTipoPago')
def AgregarEstado(request):
    if request.method == "GET":
        form = EstadoForm()
        return render(request, "cEstado.html", {'form': form})
    else:
        form = EstadoForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaEstado')
        
def AgregarCompraDetalle(request):
    if request.method == "GET":
        form = CompraDetalleForm()
        return render(request, "cCompraDetalle.html", {'form': form})
    else:
        form = CompraDetalleForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaCompraDetalle')
def AgregarCompra(request):
    if request.method == "GET":
        form = CompraForm()
        return render(request, "cCompra.html", {'form': form})
    else:
        form = CompraForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaCompra')
def AgregarEstrategia(request):
    if request.method == "GET":
        form = EstrategiaForm()
        return render(request, "cEstrategia.html", {'form': form})
    else:
        form = EstrategiaForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaEstrategia')

def AgregarEstrategiaDetalle(request):
    if request.method == "GET":
        form = EstrategiaDetalleForm()
        return render(request, "cEstrategiaDetalle.html", {'form': form})
    else:
        form = EstrategiaDetalleForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
        return redirect('TablaEstrategiaDetalle')

# Vistas de Modificar (UPDATE)

def ModificaProducto(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductoForm()
        else:
            producto = Producto.objects.get(pk=id)
            form = ProductoForm(instance= producto)
        return render(request, "eProducto.html", {'form': form})
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
        return render(request, "eFamilia.html", {'form': form})
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
        return render(request, "eSubfamilia.html", {'form': form})
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
        return render(request, "eRegion.html", {'form': form})
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
        return render(request, "eProvincia.html", {'form': form})
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
        return render(request, "eComuna.html", {'form': form})
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
        return render(request, "eSucursal.html", {'form': form})
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
        return render(request, "eTipoPago.html", {'form': form})
    else:
        if id == 0:
            form = Tipopago(request.POST)
        else:
            tipopago = Tipopago.objects.get(pk=id)
            form = TipoPagoForm(request.POST or None,request.FILES or None, instance = tipopago)
        if form.is_valid():
            form.save()
        return redirect('TablaTipoPago')


def ModificaEstado(request,id=0):
    if request.method == "GET":
        if id == 0:
            form = EstadoForm()
        else:
            producto = Estado.objects.get(pk=id)
            form = EstadoForm(instance= producto)
        return render(request, "eEstado.html", {'form': form})
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
        return render(request, "eCompraDetalle.html", {'form': form})
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
        return render(request, "eCompra.html", {'form': form})
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
        return render(request, "eEstrategia.html", {'form': form})
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
        return render(request, "eEstrategiaDetalle.html", {'form': form})
    else:
        if id == 0:
            form = EstrategiaDetalleForm(request.POST)
        else:
            producto = Estrategia_Detalle.objects.get(pk=id)
            form = EstrategiaDetalleForm(request.POST or None,request.FILES or None, instance = producto)
        if form.is_valid():
            form.save()
        return redirect('TablaEstrategiaDetalle')



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