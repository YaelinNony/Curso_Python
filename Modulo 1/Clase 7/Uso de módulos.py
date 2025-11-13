#uso de módulos en python
#! los modulos en python son archivos que contienen código python (funciones, clases,
#! variables) pueden ser reutilizados en otros programas.
#? nos ayudan a ahorrar tiempo y esfuerzo al evitar la necesidad de escribir el mismo
#? código varias veces.
#? existen modulos incorporados en python, como math, random, os, sys, entre otros.

from os import system
system("cls") # Limpiamos la consola (en Windows)
print("-"*30)
import math # Importamos la librería de matemáticas

# Para usar sus funciones, usamos el formato: libreria.funcion()
area_circulo = math.pi * (10**2)
raiz_cuadrada = math.sqrt(64)

print(f"La raíz de 64 es: {raiz_cuadrada}")
print(f"El área es: {area_circulo}")
print("-"*30)
#? otra manera de importar módulos es usando "from ... import ..."
from random import randint, choice
# Ya no necesitamos el prefijo 'random.'
numero_suerte = randint(1, 100) # Te da un número aleatorio entre 1 y 100
premios = ["Auto", "Casa", "Viaje", "Nada"]
tu_premio = choice(premios) # Elige un elemento aleatorio de la lista
print(f"Tu número de la suerte es: {numero_suerte}")
print(f"¡Ganaste: {tu_premio}!")
print("-"*30)