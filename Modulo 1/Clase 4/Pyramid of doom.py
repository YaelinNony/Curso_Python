#Buena práctica al anidar condicionales
#Evitar "Pyramid of Doom"


#un ejemplo de mala practica
# Pedimos los datos al usuario
usuario = input("Introduce tu nombre de usuario: ")
password = input("Introduce tu contraseña: ")
email = input("Introduce tu email: ")

print("\n--- Validando con el método de la 'Pirámide' ---")

# Inicia la pirámide de anidación...
if usuario != "":
    if len(password) > 8:
        if "@" in email:
            # La lógica importante está muy indentada y es difícil de encontrar
            print("✅ ¡Perfecto! Todos los datos son correctos.")
            # Aquí iría el resto del programa...
        else:
            # Los mensajes de error están en diferentes niveles de profundidad
            print("❌ Error: El email parece ser inválido.")
    else:
        print("❌ Error: La contraseña debe tener más de 8 caracteres.")
else:
    print("❌ Error: El nombre de usuario no puede estar vacío.")
#un ejemplo de buena practica
# Pedimos los datos al usuario (puedes reusar los de arriba o pedirlos de nuevo)
# usuario = input("Introduce tu nombre de usuario: ")
# password = input("Introduce tu contraseña: ")
# email = input("Introduce tu email: ")

print("\n--- Validando con el método 'Plano' y legible ---")

# Comprobamos el primer error posible
if usuario == "":
    print("❌ Error: El nombre de usuario no puede estar vacío.")

# Si el primero no ocurrió, comprobamos el segundo
elif len(password) <= 8:
    print("❌ Error: La contraseña debe tener más de 8 caracteres.")

# Si los anteriores no ocurrieron, comprobamos el último error posible
elif "@" not in email:
    print("❌ Error: El email parece ser inválido.")

# Si NINGUNO de los errores anteriores ocurrió, entonces todo está bien.
else:
    print("✅ ¡Perfecto! Todos los datos son correctos.")
    # Aquí iría el resto del programa...