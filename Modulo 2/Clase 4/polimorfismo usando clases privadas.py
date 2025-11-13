#Polimorfismo usando clases privadas
#! Técnicamente, en Python, el polimorfismo funciona exactamente igual que con los públicos. 
#! La única diferencia es la intención.
#! La intención es que este método solo sea sobrescrito por clases Hijas y no sea llamado por el código exterior.

class Motor:
    def __init__(self, cilindros):
        self.cilindros = cilindros
    
    # --- MÉTODO PROTEGIDO (Para uso interno o de Hijos) ---
    def _realizar_ignicion(self):
        print(f"Realizando ignición estándar para {self.cilindros} cilindros.")
class MotorTurbo(Motor):
    def __init__(self, cilindros, turbo_activo):
        super().__init__(cilindros)
        self.turbo_activo = turbo_activo  
    # --- SOBRESCRITURA PROTEGIDA ---
    def _realizar_ignicion(self):
        # La Hija extiende el método del Padre
        super()._realizar_ignicion() 
        if self.turbo_activo:
            print("¡Activando el TURBO!")
# --- El Polimorfismo Funciona ---
motores = [Motor(4), MotorTurbo(6, True)]
print("--- Probando motores (uso interno del sistema) ---")
for motor in motores:
    motor._realizar_ignicion() # Funciona, aunque es "protegido"
    print("-" * 10)
