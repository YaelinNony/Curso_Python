#getter en herencia
#! a herencia no rompe la encapsulación.
#? Una clase Hija NO hereda los atributos __privados del Padre.

#? Por lo tanto, la Hija DEBE usar los métodos publicos (Getters y Setters) del Padre para interactuar con esos datos.
# Forma erronea
class CuentaPadre:
    def __init__(self, saldo_inicial):
        # ATRIBUTO PROTEGIDO - ¡Mala idea!
        self._saldo = saldo_inicial
    
    def mostrar_saldo(self):
        print(f"(Padre) Saldo: {self._saldo}")

class CuentaHijaIrresponsable(CuentaPadre):
    def __init__(self, saldo_inicial):
        super().__init__(saldo_inicial)

    def deposito_corrupto(self, cantidad_str):
        # ¡PROBLEMA! La Hija ignora las reglas.
        # Puede modificar directamente el atributo del Padre.
        if cantidad_str == "mucho dinero":
            self._saldo += 1000000 # ¡Corrupción de datos!
        else:
            self._saldo += float(cantidad_str)

# --- Uso ---
cuenta_hija = CuentaHijaIrresponsable(1000)
cuenta_hija.mostrar_saldo()

print("\n--- Depositando de forma corrupta ---")
cuenta_hija.deposito_corrupto("mucho dinero")
cuenta_hija.mostrar_saldo()