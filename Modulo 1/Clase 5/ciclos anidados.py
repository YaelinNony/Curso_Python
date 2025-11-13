#anidar ciclos for dentro de otros ciclos
for i in range(1, 4):  # Ciclo externo
    print(f"Ciclo externo i={i}")
    for j in range(1, 4):  # Ciclo interno
        print(f"  Ciclo interno j={j}")
    print()  # Línea en blanco para separar las iteraciones del ciclo externo
# Ejemplo de anidamiento de ciclos for en Python
temperaturas = [50, 75, 100]
presiones = [10, 20]

print("--- Iniciando Simulación de Pruebas de Material ---")

# --- BUCLE EXTERIOR (Controla la temperatura) ---
# Se ejecutará 3 veces
for temp in temperaturas:
    
    print(f"\n--- Pruebas a {temp}°C ---")

    # --- BUCLE INTERIOR (Controla la presión) ---
    # Por CADA temperatura, este bucle se ejecutará 2 veces
    for pres in presiones:
        
        # Este código se ejecuta 3 * 2 = 6 veces
        print(f"  Ejecutando prueba: {temp}°C y {pres} psi...")
        # (Aquí iría el código de la simulación)
print("\n--- Simulación Finalizada ---")