#herencia
#! Imaginemos que queremos crear dos clases, un profesor y un alumno
#! Sabemos que se hace de la siguiente manera:
# --- El Problema (MALA PRÁCTICA) ---

class Estudiante:
    def __init__(self, nombre, edad, id_est):
        self.nombre = nombre # <-- Repetido
        self.edad = edad     # <-- Repetido
        self.id_est = id_est

    def saludar(self):       # <-- Método Repetido
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

class Profesor:
    def __init__(self, nombre, edad, num_empleado):
        self.nombre = nombre # <-- Repetido
        self.edad = edad     # <-- Repetido
        self.num_empleado = num_empleado

    def saludar(self):       # <-- Método Repetido
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
Profe_mayo = Profesor("Mayo",23,2021640157)
Profe_mayo.saludar()
