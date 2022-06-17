from django.forms import ModelForm
from .models import Compra, Producto, Familia, SubFamilia, Region, Provincia, Comuna, Tipopago, Sucursal, Estado, Estrategia, Compra_Estado, Compra_Detalle, Estrategia_Detalle

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
        fields = ['idCompra', 'fechaCompra', 'idTipopago', 'idUsuario', 'idSucursal']

class EstrategiaForm(ModelForm):
    class Meta:
        model = Estrategia
        fields = ['idEstrategia', 'nombreEstrategia']

class Compra_EstadoForm(ModelForm):
    class Meta:
        model = Compra_Estado
        fields = ['idcompra', 'idEstado', 'descripcion']

class Estrategia_DetalleForm(ModelForm):
    class Meta:
        model = Estrategia_Detalle
        fields = ['idEstrategia', 'idSucursal', 'descripcion']


class CompraDetalleForm(ModelForm):
    class Meta:
        model = Compra_Detalle
        fields = ['idcompra', 'idProducto']