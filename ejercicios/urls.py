"""
URLs para la app ejercicios (futura expansión)
"""

from django.urls import path
from . import views

app_name = 'ejercicios'

urlpatterns = [
    # ============================================
    # EJERCICIOS GENERALES
    # ============================================
    path('', views.ejercicios_list_view, name='lista'),
    path('<int:ejercicio_id>/', views.ejercicio_detalle_view, name='detalle'),
    path('<int:ejercicio_id>/resolver/', views.ejercicio_resolver_view, name='resolver'),
    
    # ============================================
    # CATEGORÍAS
    # ============================================
    path('categorias/', views.categorias_view, name='categorias'),
    path('categoria/<str:categoria>/', views.ejercicios_por_categoria_view, name='por_categoria'),
    
    # ============================================
    # API INTERNA
    # ============================================
    path('api/guardar-progreso/', views.api_guardar_progreso, name='api_guardar_progreso'),
]