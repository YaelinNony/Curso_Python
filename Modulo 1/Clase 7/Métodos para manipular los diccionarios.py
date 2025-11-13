#Metodos para manipular los diccionarios
#! al igual que las listas, los diccionarios en python tienen varios métodos 
#! incorporados que facilitan la manipulación de sus elementos.

#? algunos de los métodos más comunes para los diccionarios son:

#? 1. keys(): devuelve una vista de las claves del diccionario.
print("-"*30)
persona = {"nombre": "Carlos", "edad": 28, "ciudad": "Barcelona"}
claves = persona.keys()
print("Claves del diccionario:", claves)

#? 2. values(): devuelve una vista de los valores del diccionario.
valores = persona.values()
print("Valores del diccionario:", valores)

#? 3. items(): devuelve una vista de los pares clave-valor del diccionario.
print("Pares clave-valor del diccionario:", persona.items())

#? 4. get(): permite acceder al valor asociado a una clave, devolviendo None si la 
#? clave no existe (o un valor predeterminado si se especifica).
print("-"*30)
print("Edad usando get():", persona.get("autos"))

#? 5. pop(): elimina el par clave-valor asociado a una clave y devuelve su valor.
edad_eliminada = persona.pop("edad")
print("Edad eliminada:", edad_eliminada)
print("Diccionario después de pop():", persona)

#? update(): permite actualizar el diccionario con pares clave-valor de otro 
#? diccionario o con pares clave-valor especificados.
persona.update({"profesion": "Ingeniero", "ciudad": "Valencia"})

#? los elementos existentes se actualizan y los nuevos se agregan.
print("Diccionario después de update():", persona)

#? 7. clear(): elimina todos los elementos del diccionario.
persona.clear()
print("Diccionario después de clear():", persona)

#! estos métodos son útiles para manipular y gestionar los datos almacenados en 
#! diccionarios de manera eficiente.
#! los diccionarios se usan comúnmente para representar datos estructurados, como
#! registros de personas, configuraciones, etc.