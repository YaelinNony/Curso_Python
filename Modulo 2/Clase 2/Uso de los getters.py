#Uso de los getters
#! Los getters no son una sintaxis de python, si no un concepto de POO
#! Se usan para escribir y leer atributos privados
#? Imaginemos la siguiente situacion:
#? Vamos a un banco en donde se guarda el dinero en una boveda
#? Nosotros no podemos llegar y agarrar el dinero, necesitamos un intermediario
#! EL getter es ese intermediario que te dice cuando saldo tienes, SOLO LEE

#¿Que pasa si no usamos getters?
# --- MALA PRÁCTICA (SIN ENCAPSULACIÓN) ---
class CuentaBancariaPublica:
    def __init__(self, saldo_inicial):
        # Este atributo es PÚBLICO
        self.saldo = saldo_inicial

# --- El Caos ---
mi_cuenta = CuentaBancariaPublica(1000)
print(f"Saldo inicial: {mi_cuenta.saldo}")

# El programa no puede validar estas entradas.
mi_cuenta.saldo = -5000 
print(f"Saldo corrupto 1: {mi_cuenta.saldo}")

mi_cuenta.saldo = "¡Mucho dinero!" 
print(f"Saldo corrupto 2: {mi_cuenta.saldo}")

# Si ahora intentamos hacer una operación, el programa crasheará
try:
    mi_cuenta.saldo = mi_cuenta.saldo + 100
except TypeError as e:
    print(f"ERROR: {e}")

