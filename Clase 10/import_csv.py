import csv

# Los datos que queremos guardar
datos_alumnos = [
    ["Nombre", "Materia", "Calificacion"], # Esta es la cabecera
    ["Ana Solis", "Fisica", "9.5"],
    ["Luis Vega", "Quimica", "8.0"],
    ["Sara Orozco", "Fisica", "10.0"]
]

nombre_archivo = "datos.csv"

try:
    with open(nombre_archivo, "w", newline='') as f:
        escritor_csv = csv.writer(f)
        escritor_csv.writerows(datos_alumnos)
        
    print(f"¡Éxito! Se ha creado el archivo '{nombre_archivo}'.")

except IOError as e:
    print(f"Error al crear el archivo: {e}")