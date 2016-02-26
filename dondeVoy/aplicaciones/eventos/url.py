from django.conf.urls import patterns, include, url
from .views import RegistrarEvento , registrarEvento
from django.views.generic import TemplateView
from .forms import EventosForm

urlpatterns = patterns('',

    


   url(r'^registrarEvento/$', RegistrarEvento.as_view() , name ='RegistrarEvento'),
   url(r'^registrarEvento2/$','aplicaciones.eventos.views.registrarEvento', name='registrarEvento'),



)   
  