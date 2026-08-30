import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IEC_N4_C2_backend.settings')
django.setup()

from api.models import programmer

def populate():
    """Inserta datos de prueba en la tabla de programadores."""
    data = [
        {"fullname": "Ada Lovelace", "nickname": "ada", "age": 36, "is_active": True},
        {"fullname": "Alan Turing", "nickname": "turing", "age": 41, "is_active": True},
        {"fullname": "Guido van Rossum", "nickname": "gvanrossum", "age": 67, "is_active": True},
    ]

    for item in data:
        obj, created = programmer.objects.get_or_create(
            fullname=item["fullname"],
            defaults=item
        )
        if created:
            print(f"Creado: {obj.fullname}")
        else:
            print(f"Ya existía: {obj.fullname}")

if __name__ == '__main__':
    print("Poblando la base de datos...")
    populate()
    print("¡Proceso finalizado!")