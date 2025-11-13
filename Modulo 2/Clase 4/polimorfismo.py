#polimorfismo
#! es la consecuencia de la herencia que nos permite escribir código flexible. 
#! Es la capacidad de que objetos de diferentes clases (Hijas) respondan al mismo "mensaje" (método) de maneras únicas.

# --- 1. La Clase Padre (Superclase) ---
# Define el "contrato": todo animal tendrá un nombre
# y un método para hacer sonido.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        """Método genérico que será sobrescrito."""
        print(f"{self.nombre} hace un sonido animal genérico.")

# --- 2. Las Clases Hijas (Subclases) ---
# Cada Hija hereda de Animal y "sobrescribe" (override)
# el método 'hacer_sonido' con su propio comportamiento.

class Leon(Animal):
    def __init__(self, nombre):
        super().__init__(nombre) # Llama al constructor del Padre
    
    # --- Sobreescritura ---
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Rugido!")

class Pinguino(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    # --- Sobreescritura ---
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Graznido!")

class Serpiente(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    # --- Sobreescritura ---
    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Siseo!")

# --- 3. Creando los Objetos ---
leo = Leon("El rey leon")
pingu = Pinguino("El pinguino de OpenSource")
serpi = Serpiente("La serpiente de Python")
animal_generico = Animal("Valdivio") # Uno que NO sobrescribe

# --- 4. ¡El Polimorfismo en Acción! ---
animales_del_zoo = [leo, pingu, serpi, animal_generico]
print("--- ¡Bienvenidos al Zoológico Polimórfico! ---")
# Usamos UN solo bucle 'for' para recorrer la lista
for animal in animales_del_zoo:
    # Llamamos AL MISMO MÉTODO (.hacer_sonido()) en todos
    # Python automáticamente elige la versión correcta para cada objeto.
    animal.hacer_sonido()