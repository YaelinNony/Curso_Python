#Variables locales y globales
#! En la definicion de funciones existen dos tipos de variables:
#! Locales
#? Son variables creadas dentro de una funcion y solo existen en ella.
#? Cuando la función termina, la variable implosiona 
#! RECUERDA: el codigo exterior no puede ver lo que hay dentro de una funcion
def mi_funcion():
    variable_local = "Soy local"
    print(variable_local)
mi_funcion()
# Esta línea dará un NameError, porque 'variable_local' ya no existe.
# print(variable_local)
#! Variables globales
#? son variables creadas FUERA de una funcion
#! Las funciones pueden LEER el valor de una funcion global
#! Las funciones NO PUEDEN MODIFICAR una variable global
saldo = 1000 # Variable Global

def intentar_robar(cantidad):
    # Python cree que 'saldo' es una NUEVA variable local
    # saldo = saldo - cantidad # <-- ¡ESTO DA ERROR! (UnboundLocalError)
    
    # La forma correcta de LEERLA:
    if cantidad > saldo:
        print("¡No puedes robar más de lo que hay!")
    else:
        print("Robo exitoso (pero no cambió la global)")

intentar_robar(500)
print(f"Saldo global final: {saldo}")

#! NUNCA modifiques variables locales
saldo = 1000 # Global
#! La forma correcta es pasar la variable como parámetro y usar return para devolver el nuevo valor.
def retirar(saldo_actual, cantidad):
    if cantidad > saldo_actual:
        print("Fondos insuficientes")
        return saldo_actual # Devuelve el saldo sin cambios
    else:
        nuevo_saldo = saldo_actual - cantidad
        print(f"Retiro exitoso. Nuevo saldo: {nuevo_saldo}")
        return nuevo_saldo # Devuelve el nuevo saldo

# Así se actualiza la variable global:
saldo = retirar(saldo, 500)
saldo = retirar(saldo, 700) # Esto fallará

print(f"Saldo global final: {saldo}")