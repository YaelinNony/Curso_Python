#Uso de setters
#! Un "Setter" es un método público que valida un nuevo valor antes de asignarlo a un atributo privado.
#! Volvamos al ejemplo del banco, ahora yo quiero depositar dinero al banco
#! No puedo entrar a la boveda y meter o sacar dinero sin control, requiero un intermediario
#! Este intermediario es el Setter

#! lo que hace el setter (el cajero):
    #? Validar el dinero (que no sea falso, que la cantidad sea correcta).
    #? Si es válido, guardarlo en la bóveda (self.__saldo).
    #?Si no es válido, rechazarlo (imprimir un error).
# --- MALA PRÁCTICA (Atributos Públicos) ---
class Producto:
    def __init__(self, nombre, precio):
        # Estos atributos son PÚBLICOS
        self.nombre = nombre
        self.precio = precio
        
    def mostrar(self):
        print(f"Producto: {self.nombre}, Precio: ${self.precio}")
# Creamos un producto válido
mi_producto = Producto("Laptop", 1500)
mi_producto.mostrar()

# ¡PERO PODEMOS CORROMPER EL OBJETO DESDE FUERA!
print("\n--- Corrompiendo el objeto ---")
mi_producto.precio = -500  # 1. Un precio ilógico
mi_producto.mostrar()

mi_producto.precio = "¡Gratis!" # 2. Un tipo de dato incorrecto
mi_producto.mostrar()

# Ahora el objeto está corrupto.
# Si intentamos calcular un impuesto, el programa crasheará:
impuesto = mi_producto.precio * 0.16  # TypeError!