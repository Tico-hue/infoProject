from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from apps.perfil.models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ['username', 'email']
        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.TextInput(attrs={'class': 'form-control'}),
            }
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','aboutus','instagram','twitter','telefono']
        widgets = {
                'image':forms.FileInput(attrs={'class':'btn btn-primary'}),
                'instagram': forms.TextInput(attrs={'class': 'form-control'}),
                'aboutus': forms.TextInput(attrs={'class': 'form-control'}),
                'twitter': forms.TextInput(attrs={'class': 'form-control'}),
                'telefono': forms.TextInput(attrs={'class': 'form-control'}),

            }
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for fieldname in ['image','aboutus','instagram','twitter','telefono']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ''