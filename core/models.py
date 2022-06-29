from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group
# Create your models here.


class Tipo_usuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key= True, verbose_name ='idTipoUsuario')
    tipoUsuario = models.CharField (max_length= 100,verbose_name='tipoUsuario')
    descuento = models.FloatField

class UsuarioManager(BaseUserManager):
    def create_user(self,email,username,nombres,apellidos,password = None):
        if not email:
            raise ValueError ('El Usuario debe contar con un correo electronico')

        usuario = self.model(
            username = username, 
            email = self.normalize_email(email), 
            nombres = nombres, 
            apellidos = apellidos
        )

        usuario.set_password(password)
        usuario.usuario_administrador = True
        usuario.usuario_superuser = True
        usuario.usuario_vendedor = True
        usuario.usuario_bodeguero = True
        usuario.usuario_contador = True
        usuario.save()
        return usuario

    def create_superuser (self,email,username,nombres,apellidos,password):
        usuario = self.create_user(
            email = email,    
            username = username, 
            nombres = nombres, 
            apellidos = apellidos,
            password = password
        ) 
        usuario.save()
        return usuario


class Usuario (AbstractBaseUser):
    idUsuario = models.AutoField(primary_key= True, verbose_name ='idUsuario')
    username = models.CharField('Nombre Usuario',unique = 'True', max_length=100)
    email = models.EmailField('Correo Electronico',unique = 'True', max_length=254)
    nombres = models.CharField('Nombre', max_length=200, null = 'False')
    apellidos = models.CharField('Apellido', max_length=200, null = 'False')
    usuario_administrador = models.BooleanField( default = False)
    usuario_superuser = models.BooleanField( default = False)
    usuario_vendedor = models.BooleanField( default = False)
    usuario_bodeguero = models.BooleanField( default = False)
    usuario_contador = models.BooleanField( default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','nombres','apellidos'] 

    def _str_(self):
        return f'Usuario {self.username},{self.nombres},{self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms (self, app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador

    @property
    def is_superuser(self):
        return self.usuario_superuser
    @property
    def is_vendedor(self):
        return self.usuario_vendedor

    @property
    def is_bodeguero(self):
        return self.usuario_bodeguero
    
    @property
    def is_contador(self):
        return self.usuario_contador

class Producto (models.Model):
    idProducto = models.AutoField(primary_key= True, verbose_name ='idProducto')
    nombreProducto = models.CharField (max_length= 100,verbose_name='nombreProducto')
    precio = models.IntegerField (verbose_name ='precio')
    stock = models.IntegerField (verbose_name ='stock')
    marca = models.CharField (max_length= 50,verbose_name='marca')
    modelo = models.CharField (max_length= 50,verbose_name='modelo')
    descripcion = models.CharField (max_length= 150,verbose_name='descripcion')
    imagen = models.TextField (verbose_name='imagen')

    def __str__(self):
        return '%s' % (self.nombreProducto)

class Familia (models.Model):
    idFamilia = models.AutoField(primary_key= True, verbose_name ='idFamilia')
    nombreFamilia = models.CharField (max_length= 100,verbose_name='nombreFamilia')

    def __str__(self):
        return '%s' % (self.nombreFamilia)

class SubFamilia (models.Model):
    idSubFamilia = models.AutoField(primary_key= True, verbose_name= 'idSubFamilia')
    SubFamilia = models.CharField (max_length= 100,verbose_name='subFamilia')
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    familia = models.ForeignKey (Familia, on_delete= models.CASCADE) 

    
class Region (models.Model):
    idRegion = models.AutoField(primary_key= True, verbose_name ='idRegion')
    nombre_region = models.CharField (max_length= 30,verbose_name='nombreregion')

    def __str__(self):
        return '%s' % (self.nombre_region)

class Provincia (models.Model):
    idProvincia = models.AutoField(primary_key= True, verbose_name ='idProvincia')
    region_idRegion = models.ForeignKey(Region, on_delete= models.CASCADE)
    nombre_provincia = models.CharField (max_length= 30,verbose_name='Nombreprovincia')

    def __str__(self):
        return '%s' % (self.nombre_provincia)
    
class Comuna (models.Model):
    idComuna = models.AutoField(primary_key= True, verbose_name ='idComuna')
    Provincia_idProvincia =  models.ForeignKey(Provincia, on_delete= models.CASCADE)
    nombre_comuna = models.CharField (max_length= 30,verbose_name='NombreComuna')

    def __str__(self):
        return '%s' % (self.nombre_comuna)


class Sucursal (models.Model):
    idSucursal = models.AutoField(primary_key= True, verbose_name= 'idSucursal')
    sucursal = models.CharField (max_length= 70,verbose_name='sucursal')
    correo = models.EmailField(max_length=254,verbose_name='correo')
    telefono = models.CharField (max_length= 30,verbose_name='telefono')
    idComuna = models.ForeignKey(Comuna, on_delete= models.CASCADE)

    def __str__(self):
        return '%s' % (self.sucursal)

class Estrategia (models.Model):
    idEstrategia = models.AutoField(primary_key= True, verbose_name= 'idEstrategia')
    nombreEstrategia = models.CharField (max_length= 30,verbose_name='nombreEstrategia')

    def __str__(self):
        return '%s' % (self.nombreEstrategia)

class Estrategia_Detalle (models.Model):
    idEstrategiaDetalle = models.AutoField(primary_key= True, verbose_name ='idEstrategiaDetalle')
    idEstrategia = models.ForeignKey(Producto, on_delete= models.CASCADE)
    idSucursal = models.ForeignKey (Sucursal, on_delete= models.CASCADE)
    descripcion = models.CharField (max_length= 1000,verbose_name='descripcion')

class Tipopago (models.Model):
    idTipopago = models.AutoField(primary_key= True, verbose_name ='idTipopago')
    tipopago = models.CharField (max_length= 100,verbose_name='tipopago')

    def __str__(self):
        return '%s' % (self.tipopago)


class Estado(models.Model):
    idEstado = models.AutoField(primary_key= True, verbose_name ='idEstado')
    estado = models.CharField (max_length= 100,verbose_name='estado')

    def __str__(self):
        return '%s' % (self.estado)


class Compra (models.Model):
    idCompra = models.AutoField(primary_key= True, verbose_name ='idCompra')
    fechaCompra = models.DateField(verbose_name='Fechadecompra')
    idTipopago = models.ForeignKey (Tipopago, on_delete= models.CASCADE)
    idUsuario = models.ForeignKey (Usuario, on_delete= models.CASCADE)
    idSucursal = models.ForeignKey (Sucursal, on_delete= models.CASCADE)
    idEstado = models.ForeignKey (Estado, on_delete= models.CASCADE)


class Compra_Detalle (models.Model):
    idCompraDetalle = models.AutoField(primary_key= True, verbose_name ='idCompraDetalle')
    idcompra = models.ForeignKey (Compra, on_delete= models.CASCADE)
    idProducto = models.ForeignKey (Producto, on_delete= models.CASCADE)