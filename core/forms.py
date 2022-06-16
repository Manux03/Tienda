from django.forms import ModelForm
from .models import Producto, Familia, SubFamilia, Region, Provincia, Comuna, Tipopago, Sucursal, Estado

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
