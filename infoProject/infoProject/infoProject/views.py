from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CreateUserForm, ProductCreationForm
import os,sys
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario
from apps.productos.models import Producto
from django.urls import reverse_lazy
from django.http import Http404, HttpResponse
import json

from django.contrib.messages.views import SuccessMessageMixin



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

def busqueda(request):
    if request.is_ajax():
        valorBuscado = request.GET.get('buscando',None)
        if valorBuscado:
            resultado = Producto.objects.filter(nombre__icontains = valorBuscado) | Producto.objects.filter(descripcion__icontains = valorBuscado)

        respuesta = list()
        if resultado:
            for x in resultado:
                dic = {}
                dic['nombre'] = x.nombre
                dic['descripcion'] = x.descripcion
                respuesta.append(dic)
                salida = {'datos':respuesta,'estado':'ok'}
        else:
            salida = {'estado':'mal'}

        data = json.dumps(salida)
        return HttpResponse(data, 'application/json')
    else:
        raise Http404

def Buscar(request):
    return render(request,'base.html')

