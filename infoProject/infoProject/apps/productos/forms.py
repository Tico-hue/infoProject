from django import forms
from .models import Usuario
from .models import Producto
'''
class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'imagen']

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super(ProductCreationForm, self).__init__(*args, **kwargs)
        if user_id is not None:
            # update queryset for exercise field
            self.fields['nombre'].queryset = Usuario.objects.filter(user=user_id)
        else:
            # UserExercises.objects.none() will return an empty queryset
            self.fields['nombre'].queryset = Usuario.objects.none()
'''

class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre','descripcion','imagen','codigo']

class ModificacionProducto(forms.ModelForm):

	class Meta:
		model = Producto
		fields = ['nombre','descripcion','imagen']
