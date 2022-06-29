""""""

from django.forms import ModelForm
from core.models import Compra, Producto, Familia, SubFamilia, Region, Provincia, Comuna, Tipopago, Sucursal, Estado, Estrategia, Compra_Detalle, Estrategia_Detalle

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precio','stock','marca','modelo','descripcion','imagen']

class FamiliaForm(ModelForm):
    class Meta:
        model = Familia
        fields = ['idFamilia', 'nombreFamilia']

class SubFamiliaForm(ModelForm):
    class Meta:
        model = SubFamilia
        fields = ['idSubFamilia', 'SubFamilia', 'familia','producto']

class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['idRegion', 'nombre_region']

class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia
        fields = ['idProvincia', 'region_idRegion', 'nombre_provincia']

class ComunaForm(ModelForm):
    class Meta:
        model = Comuna
        fields = ['idComuna', 'nombre_comuna', 'Provincia_idProvincia']
    
class ComunaForm(ModelForm):
    class Meta:
        model = Comuna
        fields = ['idComuna', 'nombre_comuna', 'Provincia_idProvincia']

class SucursalForm(ModelForm):
    class Meta:
        model = Sucursal
        fields = ['idSucursal', 'sucursal', 'correo', 'telefono', 'idComuna']

class TipoPagoForm(ModelForm):
    class Meta:
        model = Tipopago
        fields = ['idTipopago', 'tipopago']

class EstadoForm(ModelForm):
    class Meta:
        model = Estado
        fields = ['idEstado', 'estado']

class CompraForm(ModelForm):
    class Meta:
        model = Compra
        fields = ['idCompra', 'fechaCompra', 'idUsuario','idTipopago', 'idSucursal','idEstado']

class EstrategiaForm(ModelForm):
    class Meta:
        model = Estrategia
        fields = ['idEstrategia', 'nombreEstrategia']

class EstrategiaDetalleForm(ModelForm):
    class Meta:
        model = Estrategia_Detalle
        fields = ['idEstrategiaDetalle','idEstrategia', 'idSucursal', 'descripcion']


class CompraDetalleForm(ModelForm):
    class Meta:
        model = Compra_Detalle
        fields = ['idCompraDetalle','idcompra', 'idProducto']
