from pyexpat import model
from django.db import models
# Create your models here.

class Producto (models.Model):
    idProducto = models.AutoField(primary_key= True, verbose_name ='idProducto')
    nombreProducto = models.CharField (max_length= 100,verbose_name='nombreProducto')
    precio = models.IntegerField (verbose_name ='precio')
    stock = models.IntegerField (verbose_name ='stock')
    marca = models.CharField (max_length= 50,verbose_name='marca')
    modelo = models.CharField (max_length= 50,verbose_name='modelo')
    descripcion = models.CharField (max_length= 50,verbose_name='descripcion')
    imagen = models.CharField (max_length= 50,verbose_name='imagen')

class Familia (models.Model):
    idFamilia = models.AutoField(primary_key= True, verbose_name ='idFamilia')
    nombreFamilia = models.CharField (max_length= 100,verbose_name='nombreFamilia')

class SubFamilia (models.Model):
    idSubFamilia = models.AutoField(primary_key= True, verbose_name= 'idSubFamilia')
    SubFamilia = models.CharField (max_length= 100,verbose_name='subFamilia')
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    familia = models.ForeignKey (Familia, on_delete= models.CASCADE) 
    
class Region (models.Model):
    idRegion = models.AutoField(primary_key= True, verbose_name ='idRegion')
    nombre_region = models.CharField (max_length= 30,verbose_name='nombreregion')

class Provincia (models.Model):
    idProvincia = models.AutoField(primary_key= True, verbose_name ='idProvincia')
    region_idRegion = models.ForeignKey(Region, on_delete= models.CASCADE)
    nombre_provincia = models.CharField (max_length= 30,verbose_name='Nombreprovincia')
    
class Comuna (models.Model):
    idComuna = models.AutoField(primary_key= True, verbose_name ='idComuna')
    Provincia_idProvincia =  models.ForeignKey(Provincia, on_delete= models.CASCADE)
    nombre_comuna = models.CharField (max_length= 30,verbose_name='NombreComuna')

class Tipo_usuario(models.Model):
    idTipoUsuario = models.AutoField(primary_key= True, verbose_name ='idTipoUsuario')
    tipoUsuario = models.CharField (max_length= 100,verbose_name='tipoUsuario')
    descuento = models.FloatField

class Usuario (models.Model):
    idUsuario = models.AutoField(primary_key= True, verbose_name= 'idUsuario')
    nombre = models.CharField (max_length= 70,verbose_name='nombre')
    apellido = models.CharField (max_length= 70,verbose_name='apellido')
    correo = models.EmailField(max_length=254,verbose_name='correo')
    idTipousuario = models.ForeignKey(Tipo_usuario, on_delete= models.CASCADE)

class Sucursal (models.Model):
    idSucursal = models.AutoField(primary_key= True, verbose_name= 'idSucursal')
    sucursal = models.CharField (max_length= 70,verbose_name='sucursal')
    correo = models.EmailField(max_length=254,verbose_name='correo')
    telefono = models.CharField (max_length= 30,verbose_name='telefono')
    idComuna = models.ForeignKey(Comuna, on_delete= models.CASCADE)

class Estrategia (models.Model):
    idEstrategia = models.AutoField(primary_key= True, verbose_name= 'idEstrategia')
    nombreEstrategia = models.CharField (max_length= 30,verbose_name='nombreEstrategia')

class Estrategia_Detalle (models.Model):
    idEstrategiaDetalle = models.AutoField(primary_key= True, verbose_name ='idEstrategiaDetalle')
    idEstrategia = models.ForeignKey(Producto, on_delete= models.CASCADE)
    idSucursal = models.ForeignKey (Sucursal, on_delete= models.CASCADE)
    descripcion = models.CharField (max_length= 1000,verbose_name='descripcion')

class Tipopago (models.Model):
    idTipopago = models.AutoField(primary_key= True, verbose_name ='idTipopago')
    tipopago = models.CharField (max_length= 100,verbose_name='tipopago')

class Estado(models.Model):
    idEstado = models.AutoField(primary_key= True, verbose_name ='idEstado')
    estado = models.CharField (max_length= 100,verbose_name='estado')

class Compra (models.Model):
    idCompra = models.AutoField(primary_key= True, verbose_name ='idCompra')
    fechaCompra = models.DateField(verbose_name='Fechadecompra')
    idTipopago = models.ForeignKey (Tipopago, on_delete= models.CASCADE)
    idUsuario = models.ForeignKey (Usuario, on_delete= models.CASCADE)
    idSucursal = models.ForeignKey (Sucursal, on_delete= models.CASCADE)
    
class Compra_Estado (models.Model):
    idCompraEstado = models.AutoField(primary_key= True, verbose_name ='idCompraEstado')
    idcompra = models.ForeignKey (Compra, on_delete= models.CASCADE)
    idEstado = models.ForeignKey (Estado, on_delete= models.CASCADE)
    descripcion = models.CharField (max_length= 100,verbose_name='descripcion')

class Compra_Detalle (models.Model):
    idCompraDetalle = models.AutoField(primary_key= True, verbose_name ='idCompraDetalle')
    idcompra = models.ForeignKey (Compra, on_delete= models.CASCADE)
    idProducto = models.ForeignKey (Producto, on_delete= models.CASCADE)