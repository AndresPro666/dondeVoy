from django.db import models
from django.contrib.auth.models import User



class Organizador(models.Model):
	user = models.OneToOneField(User)
	email = models.CharField(max_length= 80) 
	nombre = models.CharField(max_length= 50) 
	apellido = models.CharField(max_length= 50)
	dni= models.CharField(max_length= 50)
	#imagenPerfil = models.ImageField(upload_to = 'imagenesPerfil',blank=True , null= True)
	def __str__(self):
		return self.user.username

