#break y continue
# La instrucción break se utiliza para salir de un bucle antes de que haya terminado
# todas sus iteraciones.

for numero in range(10):
    if numero == 5:
        break  # Sale del bucle cuando numero es igual a 5
    print(numero)
print("Bucle terminado con break")
print("-"*20) 
# La instrucción continue se utiliza para saltar la iteración actual y pasar a la
# siguiente iteración del bucle.
for numero in range(10):
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)
print("Bucle terminado con continue")
