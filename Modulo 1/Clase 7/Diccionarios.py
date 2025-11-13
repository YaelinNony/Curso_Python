#diccionarios
#otro tipo de coleccion de datos en python
#! los diccionarios son estructuras de datos que permiten almacenar una colección de 
#! elementos no ordenados, mutables y accesibles mediante claves.

#? Los diccionarios se definen utilizando llaves {} y los elementos se almacenan en pares
#? clave-valor separados por dos puntos (:).

#? Cada clave en un diccionario debe ser única e inmutable (como cadenas, números o 
#? tuplas) mientras que los valores pueden ser de cualquier tipo de dato.

print("-"*30)
persona = {"nombre": "Ana","edad": 25,"altura": 1.65}
#podemos acceder a los valores del diccionario utilizando sus claves
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])
print("Altura:", persona["altura"])
#? de igual manera, podemos modificar los valores asociados a una clave
persona["edad"] = 26
print("Edad actualizada:", persona["edad"])
#? para agregar nuevos pares clave-valor, simplemente asignamos un valor a una nueva clave
persona["ciudad"] = "Madrid"
print("Ciudad agregada:", persona["ciudad"])
persona["Color_Favorito"]= input("Ana, ¿cuál es tu color favorito?: ")
print("Color Favorito:", persona["Color_Favorito"])
print("-"*30)