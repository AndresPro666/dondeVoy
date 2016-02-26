from django import forms
from .models import Localidad, Subcategoria , Eventos
from django.contrib.admin import widgets

class EventosForm(forms.ModelForm):
	class Meta:
		model = Eventos
		fields = ['localidad','subcategoria','nombreEvento','descripcion','fecha','calle','altura','imagenPortada']
	