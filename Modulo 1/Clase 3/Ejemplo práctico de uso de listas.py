#Ejemplo práctico de uso de listas
# --- 1. Inicio: Creando la lista (apend) ---

equipo_pokemon = []
print("--- ¡COMIENZA TU AVENTURA! ---")
print(f"Tu equipo inicial: {equipo_pokemon}")

#El usuario añader sus 3 pokemones iniciales de forma secuencial
primer_pokemon = input("\n1. Elige tu primer Pokémon para AÑADIR al equipo: ")
equipo_pokemon.append(primer_pokemon)
print(f"-> Equipo actual: {equipo_pokemon}")

segundo_pokemon = input("\n2. Elige tu segundo Pokémon: ")
equipo_pokemon.append(segundo_pokemon)
print(f"-> Equipo actual: {equipo_pokemon}")

tercer_pokemon = input("\n3. Elige tu tercer Pokémon: ")
equipo_pokemon.append(tercer_pokemon)
print(f"-> Equipo final: {equipo_pokemon}")
print("## Has usado 'append()' para añadir elementos.")
print("-"*20)

# --- 2. Añadiendo un Pokémon en un lugar específico (insert) ---
print("\n--- ¡UN POKÉMON SORPRESA SE UNE AL FRENTE! ---")
pokemon_sorpresa = input("¿Qué Pokémon apareción de repente?: ")

#Insertamos el nuevo Pokémon en la primera posición (indice 0)
equipo_pokemon.insert(0, pokemon_sorpresa)
print(f"-> {pokemon_sorpresa} toma la delantera. Equipo: {equipo_pokemon}")
print("## Has usado 'insert()' para añadir un elemento en un punto exacto.")
print("-"*20)

# --- 3. Uniendo equipos (extend) ---
print("\n--- ¡COMBINANDO FUERZAS! ---")
#Creamos una segunda lista fija para unirla a la tuya
equipo_auxiliar = ["Pikachu", "Eevee"]
print(f"Otro entrenador te presta su equipo: {equipo_auxiliar}")
equipo_pokemon.extend(equipo_auxiliar)
print(f"-> ¡Tu equipo ahora es mucho más grande!: {equipo_pokemon}")
print("## Has usado 'extend()' para fusionar tu lista con otra.")
print("-"*20)

# --- 4. Un Pokémon se va (pop y remove) ---
print("\n--- ORGANIZANDO EL EQUIPO ---")
#'pop()' elimina y nos devuelve el último elemento.
pokemon_enviado_al_pc = equipo_pokemon.pop()
print(f"El último Pokémon, '{pokemon_enviado_al_pc}', fue enviado al PC para descansar.")
print(f"-> Equipo actual: {equipo_pokemon}")
print("## Has usado 'pop()' para sacar al último elemento.")

# 'remove()' elimina un elemento por su nombre
print("\n'Pikachu' decide volver con su entrenador original.")
equipo_pokemon.remove("Pikachu")
print(f"-> Equipo tras la despedida: {equipo_pokemon}")
print("## Has usado 'remove()' para eliminar un Pokémon específico.")
print("-"*20)

# --- 5. Buscando información (index y count) ---
print("\n--- CONSULTANDO LA POKÉDEX ---")
# 'count()' es seguro de usar con cualquier entrada del usuario.
pokemon_a_contar = input("¿Qué Pokémon quieres contar en tu equipo?: ")
cantidad = equipo_pokemon.count(pokemon_a_contar)
print(f"-> Tienes {cantidad} '{pokemon_a_contar}' en tu equipo.")
print("## Has usado 'count()' para contar repeticiones.")
# 'index()' lo usamos con un valor que sabemos que existe (el primer Pokémon)
print(f"\nBuscando la posición de tu primer Pokémon, '{primer_pokemon}'...")
posicion = equipo_pokemon.index(primer_pokemon)
print(f"-> '{primer_pokemon}' está en la posición {posicion}.")
print("## Has usado 'index()' para encontrar la ubicación de un elemento.")
print("-"*20)

# --- 6. Ordenando el equipo (sort y reverse)
print("\n--- ¡PREPARANDO EL COMBATE! ---")
print(f"Tu equipo actual: {equipo_pokemon}")
equipo_pokemon.sort()
print(f"Equipo ordenado alfabéticamente: {equipo_pokemon}")
print("## Has usado 'sort()'.")

equipo_pokemon.reverse()
print(f"Equipo ordenado alfabético inverso: {equipo_pokemon}")
print("## Has usado 'reverse()'.")
print("-"*20)

# --- 7. Copiando y vaciando el equipo (copy y clear) ---
print("\n--- GUARDANDO Y TERMINANDO EL DÍA ---")
equipo_guardado = equipo_pokemon.copy()
print(f"Se ha guardado una copia de tu equipo: {equipo_guardado}")
print("## Has usado 'copy()' para crear un duplicado.")

equipo_pokemon.clear()
print(f"\nTodos tus Pokémon están descansando. Tu equipo actual está vacío: {equipo_pokemon}")
print("Has usado 'clear()' para vaciar la lista.")