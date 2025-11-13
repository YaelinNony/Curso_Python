#uso de errores y excepciones en ciclos
# --- CÓDIGO CON MANEJO DE ERRORES ---
print("--- Validador de Edad ---")
while True:
    try:
        #! 1. INTENTAMOS ejecutar este código
        edad_str = input("Introduce tu edad: ")
        edad_int = int(edad_str)
        
        # Si llegamos aquí, la conversión fue exitosa
        print(f"Correcto. Tu edad es {edad_int}.")
        break # Salimos del bucle while

    except ValueError:
        #! 2. Si el 'try' falla (porque no pudo hacer int()),
        # el programa salta aquí EN LUGAR DE CRASHEAR.
        print(f"Error: '{edad_str}' no es un número válido. Intenta de nuevo.")
print("Programa terminado.")
