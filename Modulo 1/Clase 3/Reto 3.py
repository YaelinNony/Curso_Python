# --- Reto del día 3 ---
print("\t--- BIENVENIDO --- :D \nPor favor, introduce los datos siguientes:\n")
#1. Pedir al usuario su nombre y su año de nacimiento.
nombre = input("¿Cuál es tu nombre? ")
año_de_nacimiento = int(input ("¿En qué año naciste? "))

#2. Pedir al usuario sus tres videojuegos favoritos separados por comas.
videojuegos_favoritos = input("Escribe tus 3 videojuegos favoritos, por favor, sepáralos con comas OwO: \n")

# Crear una lista llamada perfil que contenga inicialmente solo el nombre del usuario.
perfil = [nombre]

# Calculando la edad del usuario restando su año de nacimiento del año actual.
edad = 2025 - año_de_nacimiento
#Añadir la edad al final de la lista perfil.
perfil.append(edad)

# Tomando el string de los videojuegos para crear una lista de juegos
lista_de_juegos = videojuegos_favoritos.split(',')

# Extender la lista perfil con estos tres juegos.
perfil.extend(lista_de_juegos)

# Inserta el valor booleano True al principio de la lista perfil para indicar que el
# usuario está "activo".
perfil.insert(0,'True')

# El primer juego de la lista es su favorito. Quítalo de la lista usando su posición y
# guárdalo en una nueva variable llamada juego_favorito.
juego_favorito = lista_de_juegos.pop(0)

# Realiza las siguientes comprobaciones lógicas y guarda cada resultado en una variable:

# es_mayor_de_edad: El resultado de comprobar si la edad en el perfil es mayor o igual
# a 18.
es_mayor_de_edad = edad>=18

# nombre_largo: El resultado de comprobar si la longitud del nombre del usuario es mayor
# a 10 caracteres.
nombre_largo = len(nombre)>10

# es_gamer_retro: El resultado de comprobar si la palabra "pacman" está en la lista
# perfil.
es_gamer_retro = bool(perfil.count("pacman"))

# Finalmente, muestra en pantalla los siguientes resultados, cada uno en una línea:
# La lista perfil final.
# El juego_favorito.
# El resultado de es_mayor_de_edad, nombre_largo y es_gamer_retro."

print("\nCargando...")
print("-"*20)

print(f"\n¡Perfil creado con éxito! :D \n La información se muestra a continuación:\n {perfil}\n")

print("-"*20)
print(f"\nInformación adicional: ")
print(f"\nSu videojuego favorito es: {juego_favorito}")
print(f"¿Es mayor de edad? {es_mayor_de_edad}")
print(f"¿Su nombre es largo? {nombre_largo}")
print(f"¿Es gamer retro? {es_gamer_retro}")
print("-"*20)

print("\n¡Gracias por participar!, nos vemos luego OwO/")