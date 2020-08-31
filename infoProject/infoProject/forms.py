from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'apps')))
from apps.usuarios.models import Usuario

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username','email']
    
    def __init__(self,*args,**kwargs):
        super(CreateUserForm,self).__init__(*args,**kwargs)
        for campo in self.fields:
            self.fields[campo].widget.attrs.update({'class' : 'form-control'})
            self.fields[campo].help_text = None
            self.fields[campo].label = ''
            self.fields[campo].widget.attrs.update({'placeholder':campo})

