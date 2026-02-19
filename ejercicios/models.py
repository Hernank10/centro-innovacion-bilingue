from django.db import models
from django.contrib.auth.models import User

class PerfilEstudiante(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        related_name='perfil_ejercicios'
    )
    nivel = models.IntegerField(default=1)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    profesor = models.CharField(max_length=200, blank=True)  # Añadir campo profesor
    
    def __str__(self):
        return self.nombre

class Leccion(models.Model):
    titulo = models.CharField(max_length=200)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='lecciones')
    
    def __str__(self):
        return self.titulo

class Ejercicio(models.Model):
    palabra_correcta = models.CharField(max_length=100)  # Añadir campo palabra_correcta
    nivel = models.IntegerField(default=1)  # Añadir campo nivel
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='ejercicios')
    
    def __str__(self):
        return self.palabra_correcta
