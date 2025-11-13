#Construir un objeto
#! Para crear un "objeto" (una instancia) a partir de la clase, simplemente "llamamos" a la clase como si fuera una función:

# Sintaxis: class NombreDeLaClase:
class Estudiante:
    # 'pass' es un placeholder para indicar un bloque vacío
    pass
# --- Creación de Objetos (Instanciación) ---
# e1 es un objeto (una instancia) de la clase Estudiante
e1 = Estudiante() 
# e2 es OTRO objeto de la misma clase
e2 = Estudiante()
# Si los imprimimos, vemos que son cosas diferentes
# en lugares diferentes de la memoria
print(e1)
print(e2)