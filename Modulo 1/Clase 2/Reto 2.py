'''

Elabora una calculadora que le pida al usuario dos números
y realice las siguientes operaciones:
        Suma
        Resta
        Multiplicación
        División
        Módulo 2
        Potencia cúbica
        
Después de las operaciones aritméticas le pediremos al
usuario otros dos números para realizar las siguientes
operaciones:
        Asignación suma (2)
        Asignación resta (13)
        Igualdad
        Desigualdad
        Mayor que
        Menor que
        
'''
print("Bienvenido :D \n")
print("******* Calculadora *******")
n1 = int(input("Por favor, ingrese un número:"))
n2 = int(input("Por favor, ingrese otro número:"))

print("******* Operaciones *******")
print(f"La suma de {n1} + {n2} es igual a: {n1+n2}")
print(f"La resta de {n1} - {n2} es igual a: {n1-n2}")
print(f"La multiplicación de {n1} * {n2} es igual a: {n1*n2}")
print(f"El módulo 2 de {n1}: {n1%2}")
print(f"El módulo 2 de {n2}: {n2%2}")
print(f"La potencia cúbica de {n1}: {n1**3}")
print(f"La potencia cúbica de {n1}: {n2**3}")
print("**************************** \n")

print("Asignaciones y comparaciones nwn")
nc1 = int(input("Por favor, ingrese un número:"))
nc2 = int(input("Por favor, ingrese otro número:"))

print("******* Operaciones *******")
print(f"La asignación suma de {nc1} += 2 es: {nc1+2}")
print(f"La asignación suma de {nc2} += 2 es: {nc2+2}")
print(f"La asignación resta de {nc1} -= 13 es: {nc1-13}")
print(f"La asignación suma de {nc2} -= 13 es: {nc2-13}")
print(f"La igualdadad {nc1} = {nc2} es: {nc1 == nc2}")
print(f"La desigualdadad {nc1} != {nc2} es: {nc1 != nc2}")
print(f"¿Es {nc1} > {nc2}? {nc1 > nc2}")
print(f"¿Es {nc1} < {nc2}? {nc1 < nc2}")
print("**************************** \n")


'''
Extra: Realizar las tablas de verdad de las funciones
AND, OR y NOT
'''
A = 0
B = 0
print("*    Tablas de la verdad   *\n")

print("———————————————————")
print("|       AND       |")
print("———————————————————")
print("|  A  |  B  |  X  |")
print("———————————————————")
print(f"|  {A}  |  {B}  |  {int(A and B)}  |")
B += 1
print(f"|  {A}  |  {B}  |  {int(A and B)}  |")
A +=1
B-=1
print(f"|  {A}  |  {B}  |  {int(A and B)}  |")
B +=1
print(f"|  {A}  |  {B}  |  {int(A and B)}  |")
print("———————————————————")
print("\n")

print("———————————————————")
print("|       OR        |")
print("———————————————————")
print("|  A  |  B  |  X  |")
print("———————————————————")
A = 0
B = 0
print(f"|  {A}  |  {B}  |  {int(A or B)}  |")
B += 1
print(f"|  {A}  |  {B}  |  {int(A or B)}  |")
A +=1
B-=1
print(f"|  {A}  |  {B}  |  {int(A or B)}  |")
B +=1
print(f"|  {A}  |  {B}  |  {int(A or B)}  |")
print("———————————————————")
print("\n")

print("—————————————")
print("|    NOT    |")
print("—————————————")
print("|  A  |  X  |")
print("—————————————")
A = 0
print(f"|  {A}  |  {int(not A)}  |")
A = 1
print(f"|  {A}  |  {int(not A)}  |")
print("—————————————")
print("\n")