#metodo overriding
#! Para que el Polimorfismo funcione, las clases Hijas deben sobrescribir (reemplazar) el método del Padre con su propia versión
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre; self.edad = edad
        
    def mostrar_info(self):
        """Muestra la información base de la persona."""
        print(f"  Nombre: {self.nombre}")
        print(f"  Edad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, id_est):
        super().__init__(nombre, edad); self.id = id_est
        
    # --- SOBREESCRITURA CON EXTENSIÓN (Usando super()) ---
    def mostrar_info(self):
        """
        Muestra la info del Estudiante, extendiendo la del Padre.
        """
        print("--- FICHA DE ESTUDIANTE ---")
        
        # 1. Llamamos a la versión del Padre (super())
        #    para que imprima el nombre y la edad.
        super().mostrar_info() 
        
        # 2. Añadimos la información propia de la Hija
        print(f"  ID Estudiante: {self.id}")

class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad); self.materia = materia
        
    # --- SOBREESCRITURA (También) ---
    def mostrar_info(self):
        print("--- FICHA DE PROFESOR ---")
        super().mostrar_info()
        print(f"  Materia: {self.materia}")

# --- ¡LA MAGIA DEL POLIMORFISMO! ---
e1 = Estudiante("Ana Solis", 22, "101")
f1 = Profesor("Raul Vega", 45, "Física")
lista_de_personas = [e1, f1] 
print("\n\n--- INICIANDO REPORTE POLIMÓRFICO ---")
for persona in lista_de_personas:
    persona.mostrar_info()
    print("-" * 30)