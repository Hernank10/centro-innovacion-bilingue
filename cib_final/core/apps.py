<<<<<<< HEAD:core/apps.py
"""
Configuración de la aplicación Core para Academia Digital
"""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.core.checks import register, Tags
import os


class CoreConfig(AppConfig):
    """
    Configuración principal de la app Core
    Gestiona la inicialización y configuración del módulo central
    """
    
    # ============================================
    # CONFIGURACIÓN BÁSICA
    # ============================================
    
    # Nombre de la aplicación (ruta Python)
    name = 'core'
    
    # Nombre legible para humanos (aparece en el admin)
    verbose_name = _('Módulo Central')
    
    # Descripción detallada
    verbose_name_plural = _('Configuración de la Academia')
    
    # Orden de carga (valores más bajos cargan primero)
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Icono para el admin (si se usa un tema personalizado)
    icon = 'fa-solid fa-cube'
    
    # ============================================
    # METADATOS DE LA APP
    # ============================================
    
    # Versión de la app
    version = '1.0.0'
    
    # Autor
    author = 'Academia Digital Team'
    
    # Descripción
    description = _('''
        Módulo central que proporciona la funcionalidad base de la plataforma:
        - Gestión de usuarios y perfiles
        - Sistema de autenticación
        - Dashboard principal
        - Red social interna
        - Logros y estadísticas
        - Inventario y items
    ''')
    
    # ============================================
    # MÉTODO READY - INICIALIZACIÓN
    # ============================================
    
    def ready(self):
        """
        Método llamado cuando la aplicación está lista.
        Se ejecuta automáticamente al iniciar Django.
        Útil para:
        - Registrar señales (signals)
        - Configurar hooks
        - Inicializar cachés
        - Registrar checks personalizados
        """
        
        # 1. Importar señales para que se registren
        self._importar_senales()
        
        # 2. Registrar checks personalizados
        self._registrar_checks()
        
        # 3. Verificar configuración de idiomas
        self._verificar_idiomas()
        
        # 4. Crear directorios necesarios
        self._crear_directorios()
        
        # 5. Inicializar cachés si es necesario
        self._inicializar_cache()
        
        # 6. Mensaje de confirmación
        self._mostrar_banner()
    
    # ============================================
    # MÉTODOS PRIVADOS DE INICIALIZACIÓN
    # ============================================
    
    def _importar_senales(self):
        """Importa las señales para que se registren"""
        try:
            from . import signals
            # Verificar que las señales se importaron correctamente
            if hasattr(signals, 'conectar_senales'):
                signals.conectar_senales()
        except ImportError as e:
            # Si no existe el archivo de señales, crear uno básico
            self._crear_signals_basico()
        except Exception as e:
            print(f"⚠️  Error importando señales: {e}")
    
    def _registrar_checks(self):
        """Registra checks personalizados para el sistema"""
        from django.core.checks import register, Tags
        
        @register(Tags.compatibility)
        def verificar_configuracion_base(app_configs, **kwargs):
            """Verifica que la configuración base sea correcta"""
            from django.conf import settings
            errors = []
            
            # Verificar que LANGUAGES está configurado
            if not hasattr(settings, 'LANGUAGES'):
                errors.append({
                    'id': 'core.E001',
                    'msg': 'LANGUAGES no está configurado en settings.py',
                    'hint': 'Define LANGUAGES con los idiomas soportados',
                })
            
            # Verificar que LOCALE_PATHS está configurado
            if not hasattr(settings, 'LOCALE_PATHS'):
                errors.append({
                    'id': 'core.E002',
                    'msg': 'LOCALE_PATHS no está configurado en settings.py',
                    'hint': 'Define LOCALE_PATHS para las traducciones',
                })
            
            return errors
        
        print("✅ Checks personalizados registrados")
    
    def _verificar_idiomas(self):
        """Verifica la configuración de idiomas"""
        from django.conf import settings
        
        if hasattr(settings, 'LANGUAGES'):
            num_idiomas = len(settings.LANGUAGES)
            print(f"🌐 {num_idiomas} idiomas configurados")
        else:
            print("⚠️  No hay idiomas configurados")
    
    def _crear_directorios(self):
        """Crea los directorios necesarios para la app"""
        from pathlib import Path
        
        # Obtener el directorio base del proyecto
        base_dir = Path(__file__).parent.parent
        
        directorios = [
            base_dir / 'media' / 'avatares',
            base_dir / 'media' / 'logros',
            base_dir / 'static' / 'core' / 'css',
            base_dir / 'static' / 'core' / 'js',
            base_dir / 'static' / 'core' / 'img',
            base_dir / 'templates' / 'core',
            base_dir / 'logs',
        ]
        
        for directorio in directorios:
            try:
                directorio.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print(f"⚠️  No se pudo crear {directorio}: {e}")
    
    def _inicializar_cache(self):
        """Inicializa la configuración de caché"""
        from django.core.cache import cache
        
        try:
            # Probar conexión a caché
            cache.set('core_health_check', 'ok', 5)
            if cache.get('core_health_check') == 'ok':
                print("✅ Sistema de caché funcionando")
        except Exception as e:
            print(f"⚠️  Problemas con caché: {e}")
    
    def _crear_signals_basico(self):
        """Crea un archivo de señales básico si no existe"""
        import os
        from pathlib import Path
        
        signals_path = Path(__file__).parent / 'signals.py'
        
        if not signals_path.exists():
            contenido = '''"""
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
'''
            try:
                with open(signals_path, 'w', encoding='utf-8') as f:
                    f.write(contenido)
                print("✅ Archivo signals.py creado automáticamente")
            except Exception as e:
                print(f"⚠️  No se pudo crear signals.py: {e}")
    
    def _mostrar_banner(self):
        """Muestra un banner de inicio"""
        print(f"""
╔══════════════════════════════════════════════════════════╗
║             ACADEMIA DIGITAL - MÓDULO CORE               ║
╠══════════════════════════════════════════════════════════╣
║  📦 App: {self.verbose_name}                                
║  📌 Versión: {self.version}                                     
║  👤 Autor: {self.author}                                        
║  ✅ Estado: Inicializado correctamente                         
║  🔧 Configuración: Lista                                       
╚══════════════════════════════════════════════════════════╝
        """)
    
    # ============================================
    # MÉTODOS PÚBLICOS DE UTILIDAD
    # ============================================
    
    def get_info(self):
        """Retorna información de la app"""
        return {
            'name': self.name,
            'verbose_name': str(self.verbose_name),
            'version': self.version,
            'author': self.author,
            'description': str(self.description),
        }
    
    def get_models_info(self):
        """Retorna información de los modelos de la app"""
        from django.apps import apps
        models_info = []
        
        for model in apps.get_app_config(self.name).get_models():
            models_info.append({
                'name': model.__name__,
                'verbose_name': str(model._meta.verbose_name),
                'objects_count': model.objects.count(),
            })
        
        return models_info


# ============================================
# CONFIGURACIÓN POR DEFECTO
# ============================================

# Esto permite importar la configuración directamente
default_app_config = 'core.apps.CoreConfig'


# ============================================
# FUNCIÓN DE AYUDA PARA VERIFICAR ESTADO
# ============================================

def verificar_estado_core():
    """
    Función de utilidad para verificar el estado de la app core
    Uso: python manage.py shell -c "from core.apps import verificar_estado_core; verificar_estado_core()"
    """
    from django.apps import apps
    
    try:
        config = apps.get_app_config('core')
        info = config.get_info()
        
        print("\n🔍 VERIFICACIÓN DEL MÓDULO CORE")
        print("=" * 50)
        print(f"📦 App: {info['verbose_name']}")
        print(f"📌 Versión: {info['version']}")
        print(f"👤 Autor: {info['author']}")
        print(f"📝 Descripción: {info['description'][:100]}...")
        
        print("\n📊 Modelos:")
        for model in config.get_models_info():
            print(f"   ✅ {model['verbose_name']}: {model['objects_count']} registros")
        
        print("\n✅ VERIFICACIÓN COMPLETADA")
        return True
        
    except Exception as e:
        print(f"❌ Error verificando core: {e}")
        return False
=======
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = "core"
>>>>>>> 1e52048 (Guardando avances antes de sincronizar con GitHub):cib_final/core/apps.py
