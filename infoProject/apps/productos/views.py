from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import ProductCreationForm, ModificacionProducto
from .models import Usuario
from .models import Producto

# VISTA BASADA EN FUNCIONES
#def Listar(request):
#	return render(request,'productos/listar.html')
'''
@login_required
def Crear(request):
    if request.method == 'POST':
        user_id = request.user.id
        form = ProductCreationForm(user_id=user_id)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ProductCreationForm()

    return render(request, 'users/login.html', {'form': form})
'''

class Crear(LoginRequiredMixin, CreateView, Usuario):
	usuario = Usuario
	model = Producto
	form_class = ProductCreationForm
	template_name = 'productos/crear.html'
	success_url = reverse_lazy('login')

class Modificar(UpdateView):
	model = Producto
	form_class = ModificacionProducto
	template_name = 'productos/modificar.html'
	success_url = reverse_lazy('login')
