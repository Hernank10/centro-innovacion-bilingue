from django.urls import path
from . import views

app_name = 'core_api'

urlpatterns = [
    # Endpoints de API para amistades
    path('enviar-solicitud/', views.api_enviar_solicitud_amistad, name='enviar_solicitud'),
    path('responder-solicitud/', views.api_responder_solicitud, name='responder_solicitud'),
    path('enviar-mensaje/', views.api_enviar_mensaje, name='enviar_mensaje'),
    
    # Endpoints de API para items
    path('usar-item/', views.api_usar_item, name='usar_item'),
    path('equipar-item/', views.api_equipar_item, name='equipar_item'),
    
    # Endpoints de API para ranking
    path('ranking/data/', views.api_ranking_data, name='ranking_data'),
]
