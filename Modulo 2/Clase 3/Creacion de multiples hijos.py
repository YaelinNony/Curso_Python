#Creacion de multiples hijos
# (Asumimos que la clase Persona del Ejemplo 1 ya está definida)
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

# --- CLASE HIJA (HERENCIA) ---
# 1. Usamos paréntesis para indicar la herencia
class Estudiante(Persona):
    
    # 2. El constructor de la Hija (con sus parámetros únicos)
    def __init__(self, nombre, edad, id_estudiante, carrera):
        print(f"-> (Constructor de Estudiante: Creando a {nombre})")
        
        # 3. LLAMADA AL PADRE (SUPER)
        # Esto ejecuta el __init__ de Persona(self, nombre, edad)
        # y crea self.nombre y self.edad por nosotros.
        super().__init__(nombre, edad)
        
        # 4. ATRIBUTOS PROPIOS (Especialización)
        # Estos son los atributos que SÓLO el Estudiante tiene
        self.id = id_estudiante
        self.carrera = carrera
        self.__calificaciones = []

    # 5. MÉTODOS PROPIOS (Especialización)
    def registrar_calificacion(self, calif):
        """Método seguro (Setter) que solo existe en Estudiante."""
        try:
            calif_num = float(calif)
            if 0.0 <= calif_num <= 10.0:
                self.__calificaciones.append(calif_num)
                print(f"Calificación {calif_num} registrada para {self.nombre}.")
            else:
                print("Error: Calificación fuera de rango.")
        except ValueError:
            print("Error: Valor no numérico.")

# --- USO ---
print("\n--- Creando un Estudiante ---")
e1 = Estudiante("Ana Solis", 22, "101-A", "Ing. Mecatrónica")

# --- Pruebas de Herencia ---
print("\n--- Probando Métodos Heredados (¡Gratis!) ---")
# e1.saludar() -> Este método NO está definido en Estudiante.
# ¡Lo "heredó" automáticamente de Persona!
e1.saludar()
e1.cumplir_anios() # ¡Este también lo heredó!

print("\n--- Probando Métodos Propios (de Estudiante) ---")
e1.registrar_calificacion(9.5)
e1.registrar_calificacion("diez") # Prueba del try-except

print("\n--- Probando Atributos (Heredados y Propios) ---")
print(f"¿Ana está activa? {e1.esta_activo}") # Atributo de Persona
print(f"Carrera de Ana: {e1.carrera}")     # Atributo de Estudiante
class Profesor(Persona):
    def __init__(self, nombre, edad, num_empleado, materias):
        print(f"-> (Constructor de Profesor: Creando a {nombre})")
        
        # 1. Reutilizamos el constructor del Padre OTRA VEZ
        super().__init__(nombre, edad)
        
        # 2. Atributos propios
        self.num_empleado = num_empleado
        # Integramos Tupla (Módulo 1)
        self.materias = materias 
    
    # 3. Métodos propios
    def publicar_aviso(self, aviso):
        print(f"AVISO de Prof. {self.nombre}: {aviso}")

# --- USO ---
print("\n--- Creando un Profesor ---")
p1 = Profesor("Raul Vega", 45, "EMP-007", ("Física I", "Control Clásico"))

print("\n--- Probando Métodos Heredados (Profesor) ---")
p1.saludar() # También heredó saludar()

print("\n--- Probando Métodos Propios (Profesor) ---")
p1.publicar_aviso("El examen final es el 15 de diciembre.")