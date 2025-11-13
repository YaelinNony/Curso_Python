#manejo de errores y excepciones
#? existen muchas formas de romper un programa en python, como por ejemplo:
#? - dividir por cero
#? - acceder a un índice fuera de rango en una lista
#? - usar una variable no definida
#! para manejar estos errores y evitar que el programa se detenga abruptamente,
#! se utilizan las excepciones.
#? la estructura básica para manejar excepciones en python es el bloque try-except.
try:
    numero = int(input("Ingresa un número entero: "))
    resultado = 10 / numero
    print(f"El resultado de 10 dividido por {numero} es {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Debes ingresar un número entero válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
print("Programa terminado.")