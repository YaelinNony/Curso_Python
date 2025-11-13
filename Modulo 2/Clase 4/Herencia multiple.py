#Herencia multiple 
#! La Herencia Múltiple permite que una clase Hija herede de dos o más clases Padre.

#? Pensemos en un vehículo anfibio, 
#? es decir un vehiculo que hereda propiedades terrestres y acuaticas
    #? "ES UN" Coche (tiene ruedas, puede .conducir()).
    #? Y "ES UN" Barco (tiene una hélice, puede .navegar()).
    #? Para modelar esto, el VehiculoAnfibio debe heredar de ambas clases.
class PadreA_Terrestre:
    def __init__(self):
        self.ruedas = 4
        
    def conducir(self):
        print("Conduciendo en 4 ruedas...")
class PadreB_Acuatico:
    def __init__(self):
        self.helice = 1
        
    def navegar(self):
        print("Navegando con 1 hélice...")
# --- HERENCIA MÚLTIPLE ---
# La clase Hija hereda de PadreA y PadreB
class VehiculoAnfibio(PadreA_Terrestre, PadreB_Acuatico):
    def __init__(self, nombre):
        # ¡PROBLEMA! ¿Cómo llamamos a super().__init__?
        # Lo veremos en el siguiente ejemplo.
        # Por ahora, llamamos a los constructores del Padre EXPLÍCITAMENTE
        PadreA_Terrestre.__init__(self)
        PadreB_Acuatico.__init__(self)
        self.nombre = nombre
# --- Uso ---
mi_vehiculo = VehiculoAnfibio("Anfibio-007")
# 1. Tiene los métodos de PadreA
mi_vehiculo.conducir()
# 2. Tiene los atributos de PadreA
print(f"Ruedas: {mi_vehiculo.ruedas}")
# 3. Tiene los métodos de PadreB
mi_vehiculo.navegar()
# 4. Tiene los atributos de PadreB
print(f"Hélices: {mi_vehiculo.helice}")
