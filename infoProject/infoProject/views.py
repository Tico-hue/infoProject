from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import CreateUserForm
import os,sys
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario
from django.urls import reverse_lazy



class login(CreateView):
    model = Usuario
    form_class = CreateUserForm
    template_name = 'base.html'
    success_url = reverse_lazy('')

def bienahi(request):
    return render(request,'1.html')