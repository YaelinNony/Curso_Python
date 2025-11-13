#Metodo correcto para leer archivos
print("\n--- ANALIZANDO REPORTE... ---")
piezas_motor = []
try:
    with open("reporte.txt", "r") as f:
        # Esto es eficiente. 'f' actúa como un generador.
        for linea in f:
            # .strip() es ESENCIAL para limpiar el \n y espacios
            linea_limpia = linea.strip() 
            
            if "Motor" in linea_limpia:
                piezas_motor.append(linea_limpia)

    print(f"Piezas de motor encontradas: {piezas_motor}")
except FileNotFoundError:
    print("❌ ERROR: No se encontró 'reporte.txt'. Ejecuta el script de escritura primero.")