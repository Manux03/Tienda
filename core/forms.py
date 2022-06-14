from django.forms import ModelForm
from .models import Producto, Familia, SubFamilia, Region

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