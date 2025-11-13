#Solucion con getters
class CuentaBancariaSegura:
    def __init__(self, saldo_inicial):
        # 1. Hacemos el atributo PRIVADO
        self.__saldo = saldo_inicial
        self.__propietario = "Juan Pérez" # Otro dato privado
    
    # --- GETTER para el Saldo ---
    def get_saldo(self):
        """
        Este método 'Getter' nos da acceso de LECTURA
        al saldo privado.
        """
        print("... (Acceso de lectura al saldo) ...")
        return self.__saldo
        
    # --- GETTER para el Propietario ---
    def get_propietario(self):
        return self.__propietario

# --- Uso ---
mi_cuenta_segura = CuentaBancariaSegura(1000)
# Esta es la forma CORRECTA de LEER el dato:
saldo_actual = mi_cuenta_segura.get_saldo()
propietario = mi_cuenta_segura.get_propietario()

print(f"Propietario: {propietario}")
print(f"Saldo actual: {saldo_actual}")

#! Ahora tenemos un "guardián de lectura". 
#! Si quisiéramos registrar en un log cada vez que alguien consulta el saldo, podemos añadir esa lógica dentro del get_saldo().
