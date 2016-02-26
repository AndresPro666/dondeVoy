from django.db import models
from django.contrib.auth.models import User
from aplicaciones.usuarios.models import Organizador 



class Pais (models.Model):
	nombrePais = models.CharField(max_length= 50) 
	def __str__(self):
		return self.nombrePais

class Provincia (models.Model):
	nombreProvincia = models.CharField(max_length= 50) 
	pais = models.ForeignKey(Pais)
	def __str__(self):
		return self.nombreProvincia

class Localidad (models.Model):
	nombreLocalidad = models.CharField(max_length= 50)
	provincia = models.ForeignKey(Provincia)
	codigoPostal = models.CharField(max_length= 4 ) 
	def __str__(self):
		return self.nombreLocalidad


class Categoria (models.Model):
	nombreCategoria = models.CharField(max_length= 50)
	def __str__(self):
		return self.nombreCategoria

class Subcategoria (models.Model):
	nombreSubcategoria = models.CharField(max_length= 50)
	Categoria = models.ForeignKey(Categoria) 
	def __str__(self):
		return self.nombreSubcategoria



class Eventos (models.Model):
	nombreEvento = models.CharField(max_length= 50)
	descripcion = models.TextField()
	fecha = models.DateTimeField()
	estado = models.BooleanField()
	calle = models.CharField(max_length=40)
	altura=  models.CharField(max_length=5)
	imagenPortada = models.ImageField(upload_to = '/imagenesPortadas/', blank=True , null=True )
	localidad = models.ForeignKey(Localidad)
	organizador = models.ForeignKey(Organizador)
	subcategoria = models.ForeignKey(Subcategoria)
	def __str__(self):
		return self.nombreEvento



