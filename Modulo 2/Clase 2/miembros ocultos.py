#miembros ocultos
#! Esto es lo mas cercano a una clase "privada"
#!Python realmente oculta estos miembros. Si intentas acceder a objeto.__saldo desde fuera, te dará un AttributeError.

#! Python activa un mecanismo llamado Name Mangling (Modificación de Nombre), 
#! donde internamente renombra self.__saldo a algo como _NombreDeLaClase__saldo. Esto evita colisiones y lo oculta.
#! Se usan para datos criticos que nunca deben ser tocados desde fuera, excepto a través de un "guardián" (un getter o setter).

#! Usando la analogia del carro:
#? Son los pistones dentro del motor. Es imposible que el conductor los toque directamente. 
#? La única forma de moverlos es usando la interfaz pública (el pedal del acelerador).
class CuentaBancaria:
    def __init__(self, nombre, saldo_inicial):
        # ATRIBUTO PÚBLICO
        self.propietario = nombre
        
        # ATRIBUTO PRIVADO (¡oculto!)
        self.__saldo = saldo_inicial
    
    # MÉTODO PÚBLICO (Setter / Interfaz)
    def depositar(self, cantidad):
        if cantidad > 0:
            # El método SÍ puede tocar __saldo porque está DENTRO
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Error: la cantidad debe ser positiva.")
    
    # MÉTODO PÚBLICO (Getter / Interfaz)
    def get_saldo(self):
        # El método SÍ puede leer __saldo
        return self.__saldo

# --- Uso ---
mi_cuenta = CuentaBancaria("Ana", 100)

# 1. Acceso PÚBLICO (Funciona)
print(f"Propietario: {mi_cuenta.propietario}")
mi_cuenta.propietario = "Ana Solis" # Se puede modificar

# 2. Acceso PRIVADO (¡Falla!)
try:
    print(mi_cuenta.__saldo)
except AttributeError as e:
    print(f"Error al intentar leer: {e}")

try:
    mi_cuenta.__saldo = 5000 # ¡Falla!
except AttributeError as e:
    print(f"Error al intentar escribir: {e}")

# 3. Uso de la Interfaz PÚBLICA (La forma correcta)
print("\n--- Usando la interfaz pública ---")
mi_cuenta.depositar(50)
print(f"Saldo consultado: {mi_cuenta.get_saldo()}")