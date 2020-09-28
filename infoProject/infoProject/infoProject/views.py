from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CreateUserForm, ProductCreationForm
import os,sys
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario
from apps.productos.models import Producto
from django.urls import reverse_lazy

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

