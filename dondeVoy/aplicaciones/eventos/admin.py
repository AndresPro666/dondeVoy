from django.contrib import admin

from .models import Eventos , Subcategoria , Categoria , Pais , Provincia , Localidad 


admin.site.register(Eventos)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Pais)
# Register your models here.
