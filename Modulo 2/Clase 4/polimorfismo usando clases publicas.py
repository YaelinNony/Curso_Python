#polimorfismo usando clases publicas
#! Para que una clase Hija pueda sobrescribir un método, primero necesita "ver" ese método en el Padre.
#? Miembros Públicos (public): Son visibles para todos. Se pueden sobrescribir.
class FormaGeometrica:
    def __init__(self, nombre):
        self.nombre = nombre
    
    # --- MÉTODO PÚBLICO ---
    def calcular_area(self):
        print(f"Calculando el área de una {self.nombre} genérica...")
        return 0

class Circulo(FormaGeometrica):
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio
    
    # --- SOBRESCRITURA PÚBLICA ---
    def calcular_area(self):
        area = 3.14159 * (self.radio ** 2)
        print(f"Calculando área del Círculo: {area}")
        return area

# --- El Polimorfismo Funciona ---
formas = [FormaGeometrica("Forma"), Circulo("Círculo A", 10)]
for forma in formas:
    forma.calcular_area() # Python llama a la versión correcta