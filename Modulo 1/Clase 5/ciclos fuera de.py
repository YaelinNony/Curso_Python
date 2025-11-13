mediciones_voltaje = [12.5, 12.1, 12.7, 12.4, 12.6]
suma_total = 0.0 # 1. Creamos el acumulador FUERA del bucle

for voltaje in mediciones_voltaje:
    # 2. Actualizamos el acumulador DENTRO del bucle
    suma_total = suma_total + voltaje
    print(f"   Sumando {voltaje}... Suma parcial: {suma_total}")

# 3. Usamos el resultado FUERA del bucle
cantidad_mediciones = len(mediciones_voltaje)
promedio = suma_total / cantidad_mediciones

print(f"\nReporte Final:")
print(f"Suma total de voltajes: {suma_total}V")
print(f"Promedio de voltaje: {promedio:.2f}V") # :.2f redondea a 2 decimales
print(f"{voltaje}")