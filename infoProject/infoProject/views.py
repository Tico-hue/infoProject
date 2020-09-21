from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CreateUserForm
import os,sys
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario
from django.urls import reverse_lazy



class signIn(CreateView):
    model = Usuario
    form_class = CreateUserForm
<<<<<<< HEAD
    template_name = 'base.html'
    success_url = reverse_lazy('')


def bienahi(request):
    return render(request,'1.html')
=======
    template_name = 'usuarios/registro.html'
    success_url = reverse_lazy('login')
>>>>>>> b58d08e0d28488e16e57443a1cedafde32c13264
