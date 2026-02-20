"""
Señales para la aplicación core
Creado automáticamente por CoreConfig
"""

from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from .models import Perfil, Inventario, Notificacion


def conectar_senales():
    """Función para conectar todas las señales"""
    pass


@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """Crea perfil e inventario automáticamente al registrar usuario"""
    if created:
        Perfil.objects.get_or_create(usuario=instance)
        Inventario.objects.get_or_create(usuario=instance)
        
        # Notificación de bienvenida
        Notificacion.objects.create(
            usuario=instance,
            titulo="¡Bienvenido a la Academia!",
            mensaje="Completa tu perfil y comienza a aprender",
            tipo="BIENVENIDA"
        )
