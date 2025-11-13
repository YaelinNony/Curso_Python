#MRO (Method Resolution Order)
#! Que pasa si ambas clases padre tienen un metodo con el mismo nombre?
#! Python resuelve esto con algo llamado MRO (Method Resolution Order) u Orden de Resolución de Métodos.

#! La Regla del MRO (Simple): Python busca el método en un orden específico, de izquierda a derecha en la definición. 
#! El orden de búsqueda es:
    #? En la propia clase Hija (VehiculoAnfibio).
    #? Si no está ahí, en el primer Padre listado (PadreA_Terrestre).
    #? Si no está ahí, en el segundo Padre listado (PadreB_Acuatico).
    #? (Y así sucesivamente, subiendo por los "abuelos").
#! super() también sigue este orden. super() no significa "mi Padre", significa "el siguiente en la lista MRO".

class PadreA_Terrestre:
    def __init__(self):
        print("(Init Padre A: Terrestre)")
        self.ruedas = 4
        
    def reparar(self):
        print("Reparando el motor y las ruedas.")
class PadreB_Acuatico:
    def __init__(self):
        print("(Init Padre B: Acuático)")
        self.helice = 1
        
    def reparar(self):
        print("Reparando la hélice y el casco.")
# --- HERENCIA MÚLTIPLE (PadreA es el PRIMERO) ---
class VehiculoAnfibio(PadreA_Terrestre, PadreB_Acuatico):
    
    def __init__(self, nombre):
        # 1. ¿Qué pasa si usamos super()?
        print("Llamando a super().__init__...")
        super().__init__() # ¡SOLO LLAMA AL INIT DEL PRIMER PADRE!
        
        # 2. ¡Forma correcta de inicializar TODOS los padres!
        # Debemos llamarlos explícitamente por su nombre.
        print("Llamando a los inits explícitamente...")
        PadreA_Terrestre.__init__(self) # Llama al del Padre A
        PadreB_Acuatico.__init__(self) # Llama al del Padre B
        
        self.nombre = nombre
    def reparar_todo(self):
        print(f"\nReparando el {self.nombre}:")
        # 3. ¿Qué pasa si llamamos a self.reparar()?
        # Sigue el MRO: esta clase no tiene 'reparar',
        # así que busca en PadreA primero.
        print("--- Usando self.reparar() (MRO) ---")
        self.reparar() # Llama a la versión de PadreA
        # 4. ¿Cómo llamamos a AMBAS?
        print("--- Usando llamadas explícitas ---")
        PadreA_Terrestre.reparar(self)
        PadreB_Acuatico.reparar(self) 
# --- Uso ---
mi_vehiculo = VehiculoAnfibio("Anfibio-007")
mi_vehiculo.reparar_todo()