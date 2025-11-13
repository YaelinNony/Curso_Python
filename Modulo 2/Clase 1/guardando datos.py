#guardando datos
class Coche:
    # El constructor recibe los datos
    def __init__(self, color, modelo):
        print(f"Construyendo un {color} {modelo}...")
        
        # --- ATRIBUTOS ---
        # Guardamos los datos DENTRO del objeto (self)
        self.color = color
        self.modelo = modelo
        
        # También podemos crear atributos por defecto
        self.encendido = False
        self.kilometraje = 0

# --- Creación de Objetos (Instancias) ---
coche_de_ana = Coche("Rojo", "Model S")
coche_de_luis = Coche("Azul", "Mustang")

print("\n--- Objetos Creados ---")

# --- Acceso a Atributos ---
# Ahora podemos LEER los datos que guardamos
print(f"El coche de Ana es un {coche_de_ana.modelo} de color {coche_de_ana.color}")
print(f"El coche de Luis tiene {coche_de_luis.kilometraje} km")

# ¡También podemos MODIFICARLOS!
coche_de_luis.kilometraje = 100
print(f"El coche de Luis ahora tiene {coche_de_luis.kilometraje} km")

# Los objetos son independientes
print(f"El kilometraje del coche de Ana sigue siendo: {coche_de_ana.kilometraje}")