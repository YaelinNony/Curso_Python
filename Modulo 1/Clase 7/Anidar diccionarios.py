#anidar diccionarios
#? anidar diccionarios nos sirve para representar datos más complejos y estructurados.
#? podemos tener un diccionario dentro de otro diccionario, lo que nos permite organizar
#? la información de manera jerárquica.

# 1. Empezamos con el archivador vacío
base_de_datos = {}

# 2. Creamos el primer expediente (diccionario anidado)
nuevo_usuario = {
    "nombre": "Elena Garza",
    "edad": 42,
    "email": "elena.g@email.com"
}
# 3. Lo guardamos en el archivador con su clave única
base_de_datos["user_103"] = nuevo_usuario

# También puedes hacerlo directamente:
base_de_datos["user_104"] = {
    "nombre": "Juan Pérez",
    "edad": 22,
    "email": "juan.p@email.com"
}
print(base_de_datos)

#? para acceder a los datos anidados, usamos la clave del diccionario principal seguida 
#? de la clave del diccionario anidado.
print("Nombre del user_103:", base_de_datos["user_103"]["nombre"])

#? para modificar un valor en un diccionario anidado, accedemos a él de la misma manera 
#? y asignamos un nuevo valor.
base_de_datos["user_104"]["edad"] = 23
print("Edad actualizada del user_104:", base_de_datos["user_104"]["edad"])

#? para agregar un nuevo par clave-valor a un diccionario anidado, accedemos al 
#? diccionario y asignamos el nuevo par.
base_de_datos["user_103"]["telefono"] = "555-1234"
print("Teléfono agregado al user_103:", base_de_datos["user_103"]["telefono"])
print("-"*30)
#? se puede iterar sobre los diccionarios anidados utilizando bucles.
for user_id, user_info in base_de_datos.items(): #! se usa items() pasra obtener clave y valor, donde el valor es otro diccionario
    print(f"ID de Usuario: {user_id}")
    for clave, valor in user_info.items(): #! iteramos sobre el diccionario anidado
        print(f"  {clave}: {valor}")
