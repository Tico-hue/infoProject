from django import forms
from django.contrib.auth.forms import UserCreationForm
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
    

