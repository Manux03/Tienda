from pyexpat import model
from django.db import models
from sqlalchemy import true

# Create your models here.

class Producto (models.Model):
    idProducto = models.AutoField(primary_key= True, verbose_name ='idProducto')
    nombreProducto = models.CharField (max_length= 100,verbose_name='nombreProducto')
    precio = models.IntegerField (verbose_name ='precio')
    stock = models.IntegerField (verbose_name ='stock')
    marca = models.CharField (max_length= 50,verbose_name='marca')
    modelo = models.CharField (max_length= 50,verbose_name='modelo')

class Familia (models.Model):
    idFamilia = models.AutoField(primary_key= True, verbose_name ='idFamilia')
    nombreFamilia = models.CharField (max_length= 100,verbose_name='nombreFamilia')

class SubFamilia (models.Model):
    idSubFamilia = models.AutoField(primary_key= true, verbose_name= 'idSubFamilia')
    SubFamilia = models.CharField (max_length= 100,verbose_name='SubFamilia')
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    familia = models.ForeignKey (Familia, on_delete= models.CASCADE) 