from django.shortcuts import render ,render_to_response
from django.views.generic import TemplateView,FormView,ListView,CreateView 
from django.core.urlresolvers import reverse_lazy
from .models import Eventos
from .models import Organizador 	
from .forms import EventosForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect



class RegistrarEvento(FormView):
	 template_name = 'registrarEvento.html'
	 form_class = EventosForm
	 success_url = '/inicio/'
	 
	 def form_valid(self,  form ): 
		
		 return super(RegistrarEvento,self).form_valid(form)
			
		#return render_to_response('iniciar.html', {'message3': 'muchas gracias ', 'form' : form})  	

@login_required(login_url='/inicio')

def registrarEvento(request):
	form = EventosForm(request.POST or None, request.FILES or None)
	usuario1 = request.user
	if request.user.is_authenticated():	
		if Organizador.objects.filter(user=usuario1).exists():
			datos = Organizador.objects.get(user=usuario1)

			#if request.method == "POST":
			#	print (request.POST)
			
			form = EventosForm(request.POST or None, request.FILES or None)
							
			#Guarda el Formulario en bd
			
			if form.is_valid():
				instance = form.save(commit=False)
				user=request.user
				instance.user=user
				instance.save()
				return HttpResponseRedirect('/registrarEvento')
			
			context = {
				"form": form,
				"datos":datos,
			}	
			return render(request, "registrarEvento.html",context) 	
		else:	
			datos=""
			form=""
			context = {
				"form": form,
				"datos":datos,
			}
			
		return render(request, "registrarEvento.html",context) 	
	datos=""
	form=""
	context = {
		"form": form,
		"datos":datos,
		}			
	return render(request, "registrarEvento.html",context)

# Create your views here.
