from django import forms
from django.forms import ModelForm
from .models import Compra, Producto, Familia, SubFamilia, Region, Provincia, Comuna, Tipopago, Sucursal, Estado, Estrategia, Compra_Estado, Compra_Detalle, Estrategia_Detalle
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from core.models import Usuario

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

class CompraEstadoForm(ModelForm):
    class Meta:
        model = Compra_Estado
        fields = ['idCompraEstado','idcompra', 'idEstado', 'descripcion']

class EstrategiaDetalleForm(ModelForm):
    class Meta:
        model = Estrategia_Detalle
        fields = ['idEstrategiaDetalle','idEstrategia', 'idSucursal', 'descripcion']


class CompraDetalleForm(ModelForm):
    class Meta:
        model = Compra_Detalle
        fields = ['idCompraDetalle','idcompra', 'idProducto']

#userssss

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
    
class FormularioUsuario(forms.ModelForm):
    """ Formulario de Registro de un Usuario en la base de datos
    Variables:
        - password1:    Contraseña
        - password2:    Verificación de la contraseña
    """
    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña...',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese nuevamente su contraseña...',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('email','username','nombres','apellidos')
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Correo Electrónico',
                }
            ),
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }                
            ),
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            )
        }

    def clean_password2(self):
        """ Validación de Contraseña
        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.
        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormularioModifica (ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombres','apellidos','email','usuario_administrador')
        labels = {
            'nombres':'Nombres',
            'apellidos':'Apellidos',
            'email':'Email'
        }

class CustomUserCreationForm(UserCreationForm):
    pass    