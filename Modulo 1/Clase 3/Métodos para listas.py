#Métodos para listas
# ¿Qué es un método?, una función que está asociada a un objeto
# método .append() para agregar un elemento al final de una lista

lista = [1,2,3]
print(lista)
lista.append(76)
print(lista)

#método .remove() para eliminar un elemento de una lista
lista.remove(2) #Elimina la primera ocurrencia del valor 2
print(lista)

#método .pop() para eliminar un elemento de una lista por su índice
elemento_eliminado = lista.pop(0) #Elimina el elemento en el índice 0

print("Elemento eliminado: ", elemento_eliminado)
print("Lista después de pop", lista)

#método .insert() para insertar un elemento en una posición específica
lista.insert(1,10) #Inserta el valor 10 en el índice 1
print("Lista después de insert: ", lista)
lista_duplicados = [1,2,2,3,3,3]
lista_duplicados.clear()

#método .extend() para agregar los elementos de una lista a otra lista
lista1 = [1,2,3]
lista2 = [4,5,6]

lista1.extend(lista2)
print("Lista1 después de extend: ", lista1)
