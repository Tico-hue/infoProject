from django.conf import settings
from django.db import models
from apps.usuarios.models import Usuario
from apps.perfil.models import Profile
# Create your models here.

class Producto(models.Model):
	codigo = models.AutoField(primary_key = True)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nombre = models.CharField(max_length = 80)
	descripcion = models.TextField(null = True)
	imagen = models.ImageField(upload_to="productos",null = True,blank=True)
	

	def __str__(self):
		return self.nombre

	def get_product_userid(self):
		return self.usuario

	
