from django import forms
from django.contrib.auth.forms import UserCreationForm
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario
from apps.perfil.models import Profile
from django.db import transaction
class CreateUserForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre de Usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control','placeholder':'Correo Electronico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Apellido'}),
        }
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class' : 'form-control','placeholder': 'Contraseña'})
        self.fields['password2'].widget.attrs.update({'class' : 'form-control','placeholder': 'Confirme la contraseña'})
        for fieldname in ['username', 'email', 'first_name', 'last_name','password1','password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''
    
    @transaction.atomic
    def save(self):
        usuario = super().save(commit = False)
        usuario.save()
        Profile.objects.create(user= usuario)
        return usuario
