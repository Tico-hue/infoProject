from django import forms
from django.contrib.auth.forms import UserCreationForm
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario

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


