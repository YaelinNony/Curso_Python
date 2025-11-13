#! Metodos em las clases
#! Un Método es, simplemente, una función (def) que vive DENTRO de una clase.
    #? Si los atributos (self.nombre) son los sustantivos (lo que un objeto es), los métodos son los verbos (lo que un objeto hace).
    #? La Analogía del Coche: __init__ construyó el coche. Los métodos son el pedal del acelerador (.acelerar()), el pedal del freno (.frenar()) y el volante (.girar()). 
    #? Son los comportamientos que usan los atributos internos (como self.gasolina o self.ruedas).}

#! El parametro self diferencia entre programacion modular y programacion orientada a objetos
    #?self es el pronombre "yo". Es la forma en que el método accede a los atributos de ese objeto en particular.
    #? Cuando llamas a e1.mostrar_info(), Python lo traduce internamente a Estudiante.mostrar_info(e1). Pasa el objeto e1 como el primer argumento self.
class Estudiante:
    def __init__(self, nombre, id_est):
        # Atributos (Datos)
        self.nombre = nombre
        self.id = id_est
        self.calificaciones = []
        self.activo = True
    
    # --- MÉTODO 1: Un "Getter" de Información ---
    # Nota el parámetro 'self'
    def mostrar_info(self):
        """
        Este método LEE los atributos de 'self' y los imprime
        de forma ordenada.
        """
        print(f"\n--- Ficha de Estudiante ---")
        print(f"Nombre: {self.nombre}") # Accede a su propio nombre
        print(f"ID: {self.id}")         # Accede a su propio ID
        print(f"Calificaciones: {self.calificaciones}")
        
        if self.activo:
            print(f"Estado: Activo")
        else:
            print(f"Estado: Inactivo")
        print("-------------------------")

# --- Uso ---
e1 = Estudiante("Ana Solis", "101")
e2 = Estudiante("Luis Vega", "102")

# Ahora no accedemos a los datos uno por uno desde fuera.
# Le pedimos al OBJETO que nos muestre su propia información.
e1.mostrar_info()
e2.mostrar_info()