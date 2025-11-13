#ciclo while controlado por contador
# Un ciclo while controlado requiere tres elementos principales: 
# un contador, una condición y una actualización del contador.
#? el contador se inicializa antes del ciclo,
#? la condición se evalúa en cada iteración del ciclo y 
#? el contador se actualiza dentro del ciclo para evitar un ciclo infinito.

contador = 1 #contador inicializado
suma = 0 #variable para almacenar la suma de los números ingresados

while contador <= 5: #condición del ciclo
    numero = int(input("Ingrese un número: "))
    suma += numero
    contador += 1 #actualización del contador
    print(f"Has ingresado {contador - 1} números.")
print("La suma de los números ingresados es:", suma)