# cuaderno_laboratorio.py

TIPOS_ENTRADA_VALIDOS = ("Observación", "Prueba", "Error", "Mantenimiento")
ARCHIVO_LOG = "laboratorio.txt"


def registrar_entrada():
    """Solicita una nueva entrada al usuario y la guarda en el archivo."""
    print("\n--- Registrar nueva entrada ---")
    
    # Solicitar tipo de entrada válido
    tipo = input(f"Introduce el tipo de entrada {TIPOS_ENTRADA_VALIDOS}: ").strip().capitalize()
    while tipo not in TIPOS_ENTRADA_VALIDOS:
        print("❌ERROR: Tipo de entrada no válido :C. Inténtalo de nuevo.")
        tipo = input(f"Introduce el tipo de entrada {TIPOS_ENTRADA_VALIDOS}: ").strip().capitalize()

    # Solicitar descripción
    descripcion = input("Introduce la descripción de la entrada: ").strip()
    if not descripcion:
        print("❌ La descripción no puede estar vacía.")
        return
    
    # Guardar la entrada en el archivo
    try:
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(f"TIPO: {tipo} - DESCRIPCIÓN: {descripcion}\n")
        print("✅ Entrada registrada correctamente.\n")
    except Exception as e:
        print(f"⚠️ Error al guardar la entrada: {e}")


def ver_log():
    """Muestra todas las entradas registradas en el archivo."""
    print("\n--- Registro del laboratorio ---")
    try:
        with open(ARCHIVO_LOG, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                print("📭 El log está vacío.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("📭 El log está vacío o no se ha creado.")
    except Exception as e:
        print(f"⚠️ Error al leer el log: {e}")


# Crear una herramienta de terminal simple para registrar y revisar tus notas de 
# laboratorio. El programa debe guardar tus notas en un archivo de texto (.txt) 
# para que persistan, y debe ser robusto contra errores del usuario.

# Estructura de Datos inicial:
# El programa debe tener una tupla global llamada TIPOS_ENTRADA_VALIDOS que
# contenga los únicos tipos de registros permitidos: ("Observación", "Prueba",
# "Error", "Mantenimiento").
TIPOS_ENTRADA_VALIDOS = ("Observación", "Prueba", "Error", "Mantenimiento")

# Archivo de Datos (Persistencia):
# Todas las entradas del cuaderno de laboratorio se deben guardar en un archivo 
# de texto llamado "laboratorio"
with open("laboratorio.txt", "w") as f:
    f.write("--- REPORTE DE CONTROL DE LABORATORIO ---\n")
    f.write("="*41 + "\n") 

# Modularidad (Requisito Obligatorio):
# Todo el programa debe estar organizado en funciones (def). Debes tener, como
# mínimo, una función para registrar_entrada(), una para ver_log() y una función
# main() que contenga el bucle principal.

# El bucle principal debe estar limpio y solo contener el menú y las llamadas a 
# las otras funciones.

# Bucle Principal:
# El programa debe ejecutarse en un bucle continuo que muestre el menú 
# repetidamente, permitiendo al usuario realizar múltiples acciones.

# Menú de Opciones:
# En cada ciclo, el programa debe mostrar las opciones disponibles: "registrar",
# "ver_log" y "salir".

# Ejecutar Acciones (Manejo de Errores Obligatorio):
# Si el usuario escribe "registrar":
# El programa debe pedirle al usuario un tipo de entrada (ej: "Prueba").
# Debe obligar al usuario a introducir un tipo que esté dentro de la tupla 
# TIPOS_ENTRADA_VALIDOS
# Debe pedirle al usuario la descripción de la entrada (ej: "Prueba de estrés 
# del motor SN-105 iniciada").
# El programa debe añadir esta nueva entrada al final del archivo laboratorio,
# sin borrar las entradas anteriores. El formato debe ser claro, por ejemplo: 
# TIPO: Prueba - DESCRIPCIÓN: Prueba de estrés del motor SN-105 iniciada\n.

def registrar_entrada():
    """Solicita una nueva entrada al usuario y la guarda en el archivo."""
    print("\n--- Registrar nueva entrada ---")
    
    # Solicitar tipo de entrada válido
    tipo = input(f"Introduce el tipo de entrada {TIPOS_ENTRADA_VALIDOS}: ").strip().capitalize()
    while tipo not in TIPOS_ENTRADA_VALIDOS:
        print("D:ERROR: Tipo de entrada no válido :C. Inténtalo de nuevo.")
        tipo = input(f"Introduce el tipo de entrada {TIPOS_ENTRADA_VALIDOS}: ").strip().capitalize()

    # Solicitar descripción
    descripcion = input("Introduce la descripción de la entrada: ").strip()
    if not descripcion:
        print("D: Error: La descripción no puede estar vacía.")
        return
    
    # Guardar la entrada en el archivo
    try:
        with open("laboratorio.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"TIPO: {tipo} - DESCRIPCIÓN: {descripcion}\n")
        print("Entrada registrada correctamente.\n")
    except Exception as e:
        print(f"D:Error al guardar la entrada: {e}")

# Si el usuario escribe "ver_log":
# El programa debe leer y mostrar en la terminal todo el contenido del archivo
# laboratorio
# El programa no debe "crashear" si el archivo laboratorio no existe todavía;
# en su lugar, debe informar al usuario con un mensaje claro (ej: "El log está 
# vacío o no se ha creado.").

def ver_log():
    """Muestra todas las entradas registradas en el archivo."""
    print("\n--- Registro del laboratorio ---")
    try:
        with open("laboratorio.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido.strip() == "":
                print("El log está vacío.")
            else:
                print(contenido)
    except FileNotFoundError:
        print("El log está vacío o no se ha creado.")
    except Exception as e:
        print(f"Error al leer el log: {e}")

# Si el usuario escribe "salir":
# El programa debe mostrar un mensaje de despedida y terminar el bucle principal.

def main():
    while True:
        print("\n=== Cuaderno de Laboratorio ===")
        print("Opciones disponibles:")
        print("Registrar")
        print("Ver_log")
        print("Salir")

        opcion = input("Selecciona una opción: ").strip().lower()

        if opcion == "registrar":
            registrar_entrada()
        elif opcion == "ver_log":
            ver_log()
        elif opcion == "salir":
            print("Saliendo del cuaderno de laboratorio. ¡Regrese pronto :D!")
            break
        else:
            print(":c Error: Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()