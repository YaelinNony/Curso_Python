#uso de clases publicas
#! Los miembros públicos de una clase Padre son totalmente heredados por la clase Hija. 
#! La Hija puede leerlos, modificarlos y llamarlos directamente, como si fueran suyos

#? Son la interfaz principal de tu clase. Son los métodos y atributos que quieres que la clase Hija (y el resto del mundo) usen libremente.
class Padre:
    def __init__(self, nombre):
        # Atributo PÚBLICO
        self.nombre_familia = "García"
        # Atributo PÚBLICO
        self.patrimonio = 100000
    
    # Método PÚBLICO
    def saludar_familia(self):
        print(f"¡Saludos desde la familia {self.nombre_familia}!")

class Hija(Padre):
    def __init__(self, nombre, profesion):
        # Llamamos al init del padre
        super().__init__(nombre)
        self.profesion = profesion

    def mostrar_patrimonio_hija(self):
        # 1. ACCESO DIRECTO: La Hija puede LEER
        #    el atributo público del Padre.
        print(f"Accediendo al patrimonio familiar: ${self.patrimonio}")
        
    def invertir(self, cantidad):
        # 2. ACCESO DIRECTO: La Hija puede MODIFICAR
        #    el atributo público del Padre.
        print(f"Invirtiendo {cantidad} del patrimonio...")
        self.patrimonio -= cantidad
        
    def saludar_propio(self):
        # 3. ACCESO DIRECTO: La Hija puede LLAMAR
        #    el método público del Padre.
        self.saludar_familia()

# --- Uso ---
hija = Hija("Ana", "Ingeniera")

hija.mostrar_patrimonio_hija() # Lee el atributo del Padre
hija.invertir(20000)          # Modifica el atributo del Padre
hija.saludar_propio()          # Llama al método del Padre
print(f"Patrimonio restante: {hija.patrimonio}") # El mundo exterior también puede verlo