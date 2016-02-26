from django.db import models
from django.contrib.auth.models import User
from aplicaciones.usuarios.models import Organizador
from aplicaciones.eventos.models import Eventos 



class Comentarios (models.Model):
	 evento = models.ForeignKey(Eventos)
	 usuario = models.ForeignKey(User)
	 fecha = models.DateTimeField()
	 comentario = models.CharField(max_length=500)
	 def __str__(self):
		 return self.comentario 

