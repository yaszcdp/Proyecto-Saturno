from django.db import models
from django.contrib.auth.models import User

# Create your models here.
""" class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', default='avatars/default.jpg', null=True, blank=True)

    def __str__(self):
        return f'Imagen de: {self.user.username}'
    
"""