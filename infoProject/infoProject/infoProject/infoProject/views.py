from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CreateUserForm, ProductCreationForm,CustomAuthenticationForm
import os,sys
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario
from apps.productos.models import Producto
from apps.perfil.models import Profile,Rubro
from django.urls import reverse_lazy, reverse
from django.http import Http404, HttpResponse
import json
from django.contrib.auth import views as auth_views
from django.contrib.messages.views import SuccessMessageMixin

class LoginUserView(auth_views.LoginView):

	template_name = "usuarios/login.html"
	form_class = CustomAuthenticationForm
	def get_success_url(self):
		url = self.get_redirect_url()
		if url:
			return url
		elif self.request.user.is_superuser:
			return reverse("admin")
		else:
			return reverse("base")



class signIn(SuccessMessageMixin,CreateView):
	model = Usuario
	form_class = CreateUserForm
	template_name = 'usuarios/registroContenedor.html'
	success_url = reverse_lazy('login')
	success_message = " Su cuenta: %(username)s ha sido creada exitosamente "

class CreateProduct(CreateView):
	model = Producto
	form_class = ProductCreationForm
	template_name = 'productos/crear.html'
	success_url = reverse_lazy('login')

def Base(request):
	lista_rubros = list()
	lista_pares = list()
	context = {}
	rubros = Rubro.choices()
	for i in rubros:
		lista_rubros.append(i[1])
	for i in rubros:
		lista_pares.append([i[0],i[1]])

	todos = Profile.objects.all()
	context['perfiles'] = todos
	context['pares'] = lista_pares
	context['rubros'] = lista_rubros
	return render(request, 'base.html', context)

def busquedaPorRubro(request):
	print('60')
	if request.is_ajax():
		rubro = request.GET.get('porRubro',None)
		if rubro:
			rubros = Rubro.choices()
			for i in rubros:
				if rubro == i[1]:
					rubro=i[0]
			resultadoProfile =  Profile.objects.filter(rubro__icontains = rubro)
			respuesta = list()
			listaIdUsuario=list()
			if resultadoProfile:
				for objeto in resultadoProfile:
					listaIdUsuario.append(objeto.user_id)

			listaIdUsuario = list(dict.fromkeys(listaIdUsuario))
			for id in listaIdUsuario:
				dicUser={}
				dicUser['nombre'] =  Usuario.objects.filter(id__icontains = id).first().username
				dicUser['rubro'] = Profile.objects.filter(user_id__id__icontains = id).first().rubro
				dicUser['image'] = str(Profile.objects.filter(user_id__id__icontains = id).first().image)
				dicUser['aboutus'] = Profile.objects.filter(user_id__id__icontains = id).first().aboutus

				respuesta.append(dicUser)
				salida = {'datos':respuesta,'estado':'ok'}
		else:
			print('87')
			salida = {'estado':'mal'}
		data = json.dumps(salida)
		return HttpResponse(data, 'application/json')

	else:
		raise Http404

def busqueda(request):
	valorBuscado = request.GET.get('buscando',None)
	if valorBuscado:
			resultadoProd = Producto.objects.filter(nombre__icontains = valorBuscado) 
			resultadoUser = Usuario.objects.filter(username__icontains = valorBuscado)
			resultadoProfile =  Profile.objects.filter(rubro__icontains = valorBuscado)
			respuesta = list()
			listaIdUsuario=list()
			if resultadoProd:
				for objeto in resultadoProd:
					listaIdUsuario.append(objeto.usuario_id)

			if resultadoProfile:
				for objeto in resultadoProfile:
					listaIdUsuario.append(objeto.user_id)

			if resultadoUser:
				for objeto in resultadoUser:
					listaIdUsuario.append(objeto.id)
			listaIdUsuario = list(dict.fromkeys(listaIdUsuario))
			for id in listaIdUsuario:
				dicUser={}
				dicUser['nombre'] =  Usuario.objects.filter(id__icontains = id).first().username
				dicUser['rubro'] = Profile.objects.filter(user_id__id__icontains = id).first().rubro
				dicUser['image'] = str(Profile.objects.filter(user_id__id__icontains = id).first().image)
				dicUser['aboutus'] = Profile.objects.filter(user_id__id__icontains = id).first().aboutus

				respuesta.append(dicUser)
				salida = {'datos':respuesta,'estado':'ok'}
	else:
		salida = {'estado':'mal'}
	data = json.dumps(salida)
	return HttpResponse(data, 'application/json')
# def Buscar(request):
#     return render(request,'base.html')
