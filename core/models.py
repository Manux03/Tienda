from pyexpat import model
from django.db import models
from sqlalchemy import true

# Create your models here.

class Producto (models.Model):
    idProducto = models.AutoField(primary_key= True, verbose_name ='idProducto')


class Familia (models.Model):
    idFamilia = models.AutoField(primary_key= True, verbose_name ='idFamilia')

class SubFamilia (models.Model):
    idSubFamilia = models.AutoField(primary_key= true, verbose_name= 'idSubFamilia')
    producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    familia = models.ForeignKey (Familia, on_delete= models.CASCADE) 