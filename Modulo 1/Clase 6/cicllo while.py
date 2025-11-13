#ciclo while
#El ciclo while en Python se utiliza para ejecutar un bloque de código mientras una
# condición sea verdadera.

#La sintaxis básica del ciclo while es la siguiente:
bandera = True

while bandera:
    print("El ciclo while se está ejecutando.")
    # Aquí puedes agregar una condición para salir del ciclo
    respuesta = input("¿Deseas continuar? (s/n): ")
    if respuesta.lower() != 's':
        bandera = False
print("El ciclo while ha terminado.")

#while condición:
#    bloque de código
# En este ejemplo, el bloque de código dentro del ciclo while se ejecutará repetidamente
# mientras la condición sea verdadera.
# Es importante asegurarse de que la condición eventualmente se vuelva falsa para evitar
# un ciclo infinito.
# Ejemplo de in ciclo while infinito:
while True:
    print("Este ciclo while es infinito. Presiona Ctrl+C para detenerlo.")