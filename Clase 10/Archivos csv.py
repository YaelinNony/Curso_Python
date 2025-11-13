#Archivos csv
#! Un archivo CSV ("coma separated value")

import csv
# 1. Prepara tus datos (una lista de listas)
# La primera lista será la cabecera
datos_para_csv = [
    ["SensorID", "Ubicacion", "Temperatura_C", "Humedad"],
    ["SN-001", "Almacen_1", 25.4, 55],
    ["SN-002", "Laboratorio", 22.8, 40],
    ["SN-003", "Almacen_2", 26.1, 60]
]
nombre_archivo = "reporte_sensores.csv"
# 2. Abre el archivo en modo 'w' (escritura) y con newline=''
try:
    with open(nombre_archivo, "w", newline='') as f:
        # 3. Crea el "escritor"
        escritor_csv = csv.writer(f)
        
        # 4. Escribe todos los datos de golpe
        escritor_csv.writerows(datos_para_csv)
        
    print(f"¡Éxito! Se ha creado el archivo '{nombre_archivo}'.")
    print("Puedes abrirlo con Excel o Google Sheets.")
except IOError as e:
    print(f"Error: No se pudo escribir el archivo. {e}")