from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Perfiles(models.Model):
    perfil = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.perfil

class PerfilesUsuario(models.Model):
    perfil = models.ForeignKey(Perfiles,  on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=254, default='')

    def __unicode__(self):
        return self.perfil