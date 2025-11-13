#Devolviendo información
#! la funciones pueden devolver valores
#? cual es la diferencia entre print y return?
#! print: Solo muestra un valor en la pantalla. La función no "devuelve" nada.
def sumar_con_print(a, b):
    print(a + b)
resultado = sumar_con_print(5, 3)
print(f"El valor de 'resultado' es: {resultado}")
#! return: Es la forma que tiene la función de entregar un resultado para que puedas guardarlo en una variable y seguir trabajando con él.
def sumar_con_return(a, b):
    total = a + b
    return total # Entrega el valor de 'total'
    # Cualquier código después de 'return' es ignorado
# 1. Llamamos a la función
# 2. La función devuelve el valor 8
# 3. Guardamos ese 8 en la variable 'resultado'
resultado = sumar_con_return(5, 3)
print(f"El valor de 'resultado' es: {resultado}")
print(f"El doble del resultado es: {resultado * 2}")