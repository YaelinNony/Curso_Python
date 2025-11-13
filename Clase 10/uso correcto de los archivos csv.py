#uso correcto de los archivos csv
import csv

ARCHIVO_DATOS = "datos.csv"

try:
    with open(ARCHIVO_DATOS, "r", newline='') as f:
        # 1. Creamos el lector de diccionarios
        # ¡No necesitamos saltar la cabecera! La usa automáticamente.
        lector_dict_csv = csv.DictReader(f)
        
        print("\n--- Datos de Alumnos (con DictReader) ---")
        
        for fila_dict in lector_dict_csv:
            # 'fila_dict' ES UN DICCIONARIO
            # fila_dict = {'Nombre': 'Ana Solis', 'Materia': 'Fisica', 'Calificacion': '9.5'}
            
            try:
                nombre = fila_dict['Nombre']
                calificacion = float(fila_dict['Calificacion'])
                
                print(f"{nombre} obtuvo: {calificacion}")
                
            except ValueError:
                print(f"ERROR: El alumno {fila_dict.get('Nombre')} tiene una calificación inválida.")
            except KeyError:
                print("ERROR: El archivo CSV no tiene las columnas 'Nombre' o 'Calificacion'.")

except FileNotFoundError:
    print(f"ERROR CRÍTICO: No se encontró el archivo {ARCHIVO_DATOS}")
