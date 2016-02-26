from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserForm(UserCreationForm):
	email = forms.CharField()
	nombre = forms.CharField()
	apellido = forms.CharField()
	dni= forms.CharField()
	#imagenPerfil = forms.ImageField()