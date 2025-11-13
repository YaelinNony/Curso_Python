#set
# El set es otra estructura de datos en python que permite almacenar una colección de 
# elementos únicos y desordenados.

#! A diferencia de las listas y tuplas, los sets no permiten elementos duplicados y no 
#! mantienen un orden específico.

#? Los sets se definen utilizando llaves {} o la función set().
#? Los elementos de un set deben ser inmutables (como cadenas, números o tuplas), 
#? pero el set en sí es mutable.

#? podemos crear un set de la siguiente manera:
conjunto1 = {1, 2, 3, 4, 5}
print("Conjunto 1:", conjunto1)
conjunto2 = set(["a", "b", "c", "d"])
print("Conjunto 2:", conjunto2)

#! El beneficio de usar serts es que automáticamente eliminan los elementos duplicados.
#! permite realizar operaciones matemáticas como unión, intersección y diferencia de 
#! conjuntos. Es mas rapido para verificar la pertenencia de un elemento en comparación
#! con listas o tuplas.
print("-"*30)

#? metodos comunes para manipular sets:
#? 1. add(): agrega un elemento al set.
conjunto1.add(6)
print("Conjunto 1 después de add():", conjunto1)
#? 2. remove(): elimina un elemento del set. Lanza un error si el elemento no existe.
conjunto1.remove(3)
print("Conjunto 1 después de remove():", conjunto1)
#? 3. discard(): elimina un elemento del set. No lanza error si el elemento no existe.
conjunto1.discard(10)  # No lanza error
print("Conjunto 1 después de discard():", conjunto1)
#? 4. union(): devuelve un nuevo set que es la unión de dos sets.
conjunto_union = conjunto1.union({7, 8, 9})
#? 5. intersection(): devuelve un nuevo set que es la intersección de dos sets.
conjunto_interseccion = conjunto1.intersection({4, 5, 6, 7})
print("Conjunto Unión:", conjunto_union)
print("Conjunto Intersección:", conjunto_interseccion)
#? 6. difference(): devuelve un nuevo set con los elementos que están en el primer set
#? pero no en el segundo.
conjunto_diferencia = conjunto1.difference({4, 5})
print("Conjunto Diferencia:", conjunto_diferencia)
#? 7. clear(): elimina todos los elementos del set.
conjunto1.clear()
print("Conjunto 1 después de clear():", conjunto1)
print("-"*30)

#! los sets son útiles cuando se necesita almacenar una colección de elementos únicos y
#! realizar operaciones de conjuntos.
print("Uso practico de sets:")
prototipo_1_componentes = {"motor", "ruedas", "chasis", "batería"}
prototipo_2_componentes = {"motor", "alerón", "chasis", "computadora"}

# .union() o | (Barra vertical): Todos los elementos de ambos
todos_los_componentes = prototipo_1_componentes.union(prototipo_2_componentes)
print(f"Unión: {todos_los_componentes}")

# .intersection() o & (Ampersand): Solo los elementos en común
componentes_comunes = prototipo_1_componentes.intersection(prototipo_2_componentes)
print(f"Intersección: {componentes_comunes}")

# .difference() o - (Guion): Elementos que están en el primero, pero NO en el segundo
solo_en_proto_1 = prototipo_1_componentes.difference(prototipo_2_componentes)
print(f"Solo en 1: {solo_en_proto_1}")
print("-"*30)

#! los sets se usan Cuando el orden no importa y la unicidad sí. 
#! Para eliminar duplicados, para comparar dos listas y ver qué tienen en común o qué
#! tienen de diferente.