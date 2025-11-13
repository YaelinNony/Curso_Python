#parametros en funciones
#! Las funciones pueden recibir datos, esto las vuelve muy poderosas.
# 'nombre' es el PARÁMETRO
def saludar_a(nombre):
    print(f"¡Hola, {nombre}! Bienvenido.")
# "Ana" y "Luis" son los ARGUMENTOS
saludar_a("Ana")
saludar_a("Luis")

#! las funciones pueden recibir multiples parámetros
def sumar(a, b):
    print(f"La suma de {a} y {b} es: {a + b}")
sumar(5, 3)
sumar(100, 200)