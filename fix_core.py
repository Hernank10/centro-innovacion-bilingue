#!/usr/bin/env python
import os
from pathlib import Path

def fix_core():
    print("🔧 CORRIGIENDO CORE APP")
    print("=" * 60)
    
    # Verificar que core/models.py existe
    models_file = Path('core/models.py')
    if models_file.exists():
        print("✅ core/models.py encontrado")
    else:
        print("❌ core/models.py NO encontrado")
        return
    
    # Verificar qué modelos existen
    with open(models_file, 'r') as f:
        content = f.read()
        modelos = []
        for line in content.split('\n'):
            if 'class ' in line and '(' in line and '):' in line:
                modelo = line.split('class ')[1].split('(')[0].strip()
                modelos.append(modelo)
        
        print(f"\n📊 Modelos encontrados: {', '.join(modelos)}")
    
    # Verificar core/admin.py
    admin_file = Path('core/admin.py')
    if admin_file.exists():
        with open(admin_file, 'r') as f:
            admin_content = f.read()
            
        # Verificar importaciones
        importaciones = []
        for modelo in modelos:
            if modelo in admin_content:
                print(f"✅ {modelo} importado correctamente")
            else:
                print(f"❌ {modelo} NO está en admin.py")
    
    print("\n" + "=" * 60)
    print("\n✅ VERIFICACIÓN COMPLETADA")

if __name__ == '__main__':
    fix_core()
