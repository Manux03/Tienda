from django.forms import ModelForm
from .models import Producto, Familia

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['idProducto', 'nombreProducto', 'precio','stock','marca','modelo','descripcion','imagen']

class FamiliaForm(ModelForm):
    class Meta:
        model = Familia
        fields = ['idFamilia', 'nombreFamilia']