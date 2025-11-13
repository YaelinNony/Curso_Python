#Listas
#Las listas son elementos que permiten almacenar varios valores en una sola variable
#se definen con corchetes []
#Los elementos de una lista se separan por comas

mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)
materiales = ["Acero", "Cobre", "Aluminio", "Plomo"]
print(materiales)

#Los elementos de una lista pueden ser de diferentes tipos de datos
otra_lista = ["hola", 1, 2.5, True]
print(otra_lista)

#Las listas pueden contener otras listas
lista_anidada = [1,2, [3, 4], 5]
print(lista_anidada)

#Cada elemento de la lista tiene una posición única llamada índice, que comienza en 0
print("Primer elemento de la lista mi_lista: ", mi_lista[0])
print("Segundo elemento de la lista materiales: ", materiales[1])

#Cómo obtener el último elemento de una lista sin saber su longitud
print("Último elemento de la lista otra_lista: ", otra_lista[-1])