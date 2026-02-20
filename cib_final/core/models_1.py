from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Perfil(models.Model):
    usuario = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='perfil_core'
    )
    nombre_completo = models.CharField(max_length=200, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    puntos_totales = models.IntegerField(default=0)
    nivel_maestria = models.IntegerField(default=1)
    racha_actual = models.IntegerField(default=0)
    racha_maxima = models.IntegerField(default=0)
    fecha_registro = models.DateTimeField(default=timezone.now)
    ultima_conexion = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuario.username}"
