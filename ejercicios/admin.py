from django.contrib import admin
from .models import PerfilEstudiante, Curso, Leccion, Ejercicio

@admin.register(PerfilEstudiante)
class PerfilEstudianteAdmin(admin.ModelAdmin):
    list_display = ['user', 'nivel']
    search_fields = ['user__username']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'profesor']  # Usar 'nombre' en lugar de 'profesor'
    search_fields = ['nombre']

@admin.register(Leccion)
class LeccionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'curso']
    list_filter = ['curso']

@admin.register(Ejercicio)
class EjercicioAdmin(admin.ModelAdmin):
    list_display = ['id', 'palabra_correcta', 'nivel', 'leccion']  # Campos que existen
    list_filter = ['nivel', 'leccion']
    search_fields = ['palabra_correcta']
