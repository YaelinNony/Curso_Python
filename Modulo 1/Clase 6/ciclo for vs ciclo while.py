#ciclo for vs ciclo while
# La diferencia entre un ciclo for y un ciclo while es que el ciclo for itera sobre una
# secuencia (como una lista, tupla, diccionario, conjunto o cadena)
# y el ciclo while repite un bloque de código mientras una condición sea verdadera.

#! ¿Caundo usar un ciclo for?
#! cuando se conoce el número de iteraciones o se itera sobre una secuencia.

print("Contaremos los numeros divisibles entre 5 en un rango del 1 al 100")
for numero in range(1, 101):
    if numero % 5 == 0:
        print(numero)
print(f"Hay {100//5} numeros divisibles entre 5 en un rango del 1 al 100")

#! ¿Cuando usar un ciclo while?
#! cuando no se sabe cuántas veces se repetirá el bloque de código y depende de una 
#! condición.
print("-"*30)
print("Jugemos un juego, adivina el numero que estoy pensando entre el 1 y el 10")
numero_secreto= 5
numero_intentos= 1
while True:
    intentos = int(input("¿En que número estoy pensando?: "))
    if intentos < 1 or intentos > 10:
        print("Bobo, el numero debe estar entre 1 y 10")  # valida que el numero este entre 1 y 10
        numero_intentos += 1
        continue
    elif intentos == numero_secreto:
        print("¡Correcto!, el numero que estaba pensando era el: ", numero_secreto)
        break
    else:
        print("Error, llevas ", numero_intentos, "intentos, intenta de nuevo.")
        numero_intentos += 1
print("Juego terminado, lo lograste en ", numero_intentos, "intentos.")
