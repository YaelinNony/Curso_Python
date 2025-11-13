#manejo de errores en listas
# --- CÓDIGO CON MANEJO DE ERRORES ---
inventario = ["Poción", "Espada", "Escudo"]
print(f"Tu inventario es: {inventario}")
print("Índices disponibles: 0, 1, 2")
while True:
    try:
        # 1. Intentamos obtener el índice
        indice_str = input("¿Qué índice de ítem quieres inspeccionar? ")
        indice = int(indice_str)   
        # 2. Intentamos usar el índice
        print(f"Has seleccionado: {inventario[indice]}")
    #! Podemos "anidar" excepciones para atrapar diferentes errores
        break  # Salimos del bucle si todo salió bien
    except ValueError:
        print("❌ Error: Debes introducir un NÚMERO (0, 1, o 2).")
    except IndexError:
        # 3. Si el 'int()' funcionó pero el índice estaba fuera de rango
        print(f"❌ Error: ¡Ese índice no existe! Solo tienes {len(inventario)} ítems.")