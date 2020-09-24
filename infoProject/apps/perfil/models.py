from django.db import models
from apps.usuarios.models import Usuario
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default-user-image.jpg', upload_to='profile_pics')
    aboutus = models.TextField(default="Sobre nosotros...")
    instagram = models.CharField(max_length=30, default="Instagram...")
    twitter = models.CharField(max_length=30, default="@Twitter...")
    telefono = models.BigIntegerField(default=0)
    

    def __str__(self):
        return f'Perfil de {self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
