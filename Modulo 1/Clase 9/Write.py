from datetime import datetime
# --- Ejemplo 2: Creando un Log de Errores
now = datetime.now()
def guardar_error(tipo_error, modulo):
    """
    Esta función AÑADE un error a un log sin borrar los anteriores.
    """
    timestamp = now 
    
    # Preparamos las líneas con el salto de línea incluido
    lineas_a_escribir = [
        f"ERROR: {timestamp}\n",
        f"  Modulo: {modulo}\n",
        f"  Tipo: {tipo_error}\n",
        "--------------------\n"
    ]
    with open("errores.log", "a") as f:
        f.writelines(lineas_a_escribir)
    print("Error registrado en el log.")
try:
    int("hola") # Esto fallará
except ValueError as e:
    guardar_error(str(e), "modulo_principal")
#! Si este programa se ejecuta repetidad veces el log de errores irá creciendo
