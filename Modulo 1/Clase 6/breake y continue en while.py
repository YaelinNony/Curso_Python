#esto tambien se puede usar en while
contador = 0
while contador < 10:
    contador += 1
    if contador == 7:
        break  # Sale del bucle cuando contador es igual a 7
    if contador % 2 == 0:
        continue  # Salta los números pares
    print(contador)
#o en ejemplos con while true
while True:
    entrada = input("Escribe 'salir' para terminar el bucle: ")
    if entrada.lower() == 'salir':
        break  # Sale del bucle si el usuario escribe 'salir'
    print(f"Has escrito: {entrada}")
print("Bucle terminado con break y continue en while")