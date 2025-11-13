#archivos
#! Los programas en python tienen una memoria VOLATIL
#! Es decir, los valores de las variables desaparecen cuando el programa termina
#! Uno de los métodos que se usa para almacenar los datos de manera PERMANENTE es usar archivos
#! En este caso usaremos archivos de texto (.TXT)
# --- Ejemplo 1: Creando un Reporte (Modo 'w') ---
piezas_aprobadas = ["SN-101-Motor", "SN-103-Chasis", "SN-104-Sensor"]
# 'w' borra el archivo anterior si existía
with open("reporte.txt", "w") as f:
    f.write("--- REPORTE DE CONTROL DE CALIDAD ---\n")
    f.write(f"Total de piezas aprobadas: {len(piezas_aprobadas)}\n")
    f.write("="*20 + "\n") # Escribimos un separador
    
    for pieza in piezas_aprobadas:
        # ¡La clave está en añadir el '\n' manualmente!
        f.write(f"Pieza: {pieza}\n")
print("¡'reporte.txt' creado!")
