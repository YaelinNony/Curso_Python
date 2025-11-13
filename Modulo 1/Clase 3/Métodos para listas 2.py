lista = [1,2,3]

#método .lent() para obtener la longitud de una lista
print(f"Longitud de la lista: {len(lista)}")

#método .sort() para ordenar los elementos de una lista
lista_numeros = [3,1,4,2]
print(f"Lista desordenada: {lista_numeros}")
lista_numeros.sort() #Ordena la lista en orden ascendente
print("Lista ordenada:", lista_numeros)

#método .revere() para invertir el orden de los elementos de una lista
lista_numeros.reverse()
print("Lista invertida:", lista_numeros)

#método .count() para contar cuántas veces aparece un elemento en una lista
lista_duplicados = [1,2,2,3,3,3]
print(f"Lista con duplicados: {lista_numeros}")
print("El número 2 aparece", lista_duplicados.count(2)," veces")
print("El número 3 aparece", lista_duplicados.count(3)," veces")