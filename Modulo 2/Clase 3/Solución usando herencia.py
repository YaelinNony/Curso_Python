#Solución usando herencia
#! Es uno de los 4 pilares de la POO
#! Nos permite definir una Clase Padre (o Superclase) que contiene toda la lógica y atributos comunes. 
#! Luego, podemos crear Clases Hijas (o Subclases) que "heredan" automáticamente todo lo del padre.
#! El Principio Clave: La Relación "ES UN/UNA" (IS A) La herencia solo tiene sentido si hay una relación lógica de "ES UN/UNA".
    #? Un Estudiante ES UNA Persona.
    #? Un Profesor ES UNA Persona.
    #? (Pero un Coche NO ES UNA Persona).
class Persona:
    """
    Esta es la Superclase. Contiene todos los atributos
    y métodos comunes que cualquier "Persona" en nuestro
    sistema tendrá.
    """
    def __init__(self, nombre, edad):
        print(f"(Constructor de Persona: Creando a {nombre})")
        self.nombre = nombre
        self.edad = edad
        self.esta_activo = True # Todas las personas empiezan activas
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! {self.nombre} ahora tiene {self.edad} años.")
# --- Uso de la clase Padre ---
print("--- Creando una Persona genérica ---")
p1 = Persona("Juan Pérez", 40)
p1.saludar()