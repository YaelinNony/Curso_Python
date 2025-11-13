#archivos json
#! JSON (JavaScript Object Notation) es un formato de texto, pero no es solo texto. Es un lenguaje universal para describir datos complejos.
#? Un .txt es un diario.
#? Un .csv es una tabla de Excel.
#? Un .json son los planos de un edificio. Describe una estructura compleja, 
#? con habitaciones (listas) y objetos (diccionarios) anidados unos dentro de otros.

import json

# Nuestra base de datos del reto (Dict anidado - Día 7)
db_alumnos = {
    "101": {
        "nombre": "Ana Solis",
        "curso": "Física",
        "calificaciones": [9.5, 8.0, 10.0]
    },
    "102": {
        "nombre": "Luis Vega",
        "curso": "Química",
        "calificaciones": [7.0, 8.5, 8.0]
    }
}

ARCHIVO_JSON = "mi_base_de_datos.json"

print("Iniciando guardado de base de datos...")
try:
    # Abrimos en modo 'w' (escritura), igual que con .txt
    with open(ARCHIVO_JSON, "w") as f:
        # ¡La magia! Vuelca el diccionario 'db_alumnos' al archivo 'f'
        json.dump(db_alumnos, f, indent=4)
        
    print(f"✅ ¡Éxito! Base de datos guardada en '{ARCHIVO_JSON}'")

except IOError as e:
    # Error de permisos, disco lleno, etc. (Día 11)
    print(f"❌ ERROR CRÍTICO: No se pudo escribir en el archivo. {e}")