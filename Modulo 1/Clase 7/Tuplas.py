#Tipos de estructuras de datos
#? En python existen varios tipos de estructuras de datos, entre ellas las tuplas.
#? Las tuplas son estructuras de datos que permiten almacenar una colección de elementos
#? ordenados e inmutables.

#! es decir, una vez que se crea una tupla, no se pueden modificar sus elementos
#! (no se pueden agregar, eliminar o cambiar elementos).

#? Las tuplas se definen utilizando paréntesis () y los elementos se separan por comas.
coordenadas = (10.0, 20.0)
print(coordenadas)

#? Las tuplas pueden contener elementos de diferentes tipos de datos, como enteros, 
#? cadenas, flotantes, etc.
persona = ("Juan", 30, 1.75)
print(persona)

#? Se pueden acceder a los elementos de una tupla utilizando índices, al igual que las 
#? listas.
print("Nombre:", persona[0])
print("Edad:", persona[1])
print("Estatura:", persona[2])

#? Las tuplas también permiten el desempaquetado, lo que significa que se pueden asignar
#? los elementos de una tupla a variables individuales.
nombre, edad, estatura = persona
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)

#? Aunque las tuplas son inmutables, se pueden realizar algunas operaciones como 
#? concatenación y repetición.
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
# Concatenación
tupla3 = tupla1 + tupla2
print("Tupla concatenada:", tupla3)
# Repetición
tupla4 = tupla1 * 2
print("Tupla repetida:", tupla4)
#? Las tuplas también tienen métodos incorporados, como count() y index().
numeros = (1, 2, 3, 2, 4, 2)
print("Número de veces que aparece el 2:", numeros.count(2))
print("Índice del primer 3:", numeros.index(3))

#! las tuplas son útiles cuando se desea almacenar datos que no deben cambiar a lo largo 
#! del tiempo como coordenadas geográficas, fechas, etc.