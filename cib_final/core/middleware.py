# core/middleware.py
from django.utils import translation
from django.conf import settings

class ForceDefaultLanguageMiddleware:
    """
    Middleware que fuerza el idioma por defecto si no hay prefijo en la URL
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verificar si la URL ya tiene prefijo de idioma
        path = request.path_info
        has_lang_prefix = any(
            path.startswith(f'/{lang_code}/') 
            for lang_code, _ in settings.LANGUAGES
        )
        
        if not has_lang_prefix and path != '/':
            # Redirigir a la misma URL con el idioma por defecto
            from django.shortcuts import redirect
            return redirect(f'/{settings.LANGUAGE_CODE}{path}')
        
        return self.get_response(request)
