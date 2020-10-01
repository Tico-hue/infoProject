from django.db import models
from apps.usuarios.models import Usuario
from PIL import Image
from enum import IntEnum

class Rubro(IntEnum):
    OTROS = 1
    INDUMENTARIA = 2
    CERVECERIA = 3
    COSMETICO = 4
    SERVICIOS = 5


    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    @classmethod
    def crearRubro(cls):
        pass

class Profile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default-user-image.jpg', upload_to='profile_pics')
    aboutus = models.TextField(default="Sobre nosotros...")
    instagram = models.CharField(max_length=30, default="Instagram...")
    twitter = models.CharField(max_length=30, default="@Twitter...")
    telefono = models.BigIntegerField(default=0)
    rubro = models.IntegerField(choices=Rubro.choices(), default=Rubro.OTROS)

    

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        print(img)
        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
