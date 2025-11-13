#funciones lambda
#! es una función pequeña, de una sola línea, y desechable, como una nota tipo post-it
#? usualmente se usan como argumentos para otras funciones
# Guardamos la función lambda en una variable (aunque no es su uso principal)
duplicar_lambda = lambda x: x * 2

print(duplicar_lambda(5))
#! Uno de los usos caracteristicos de lambda es usarlas como argumentos para funciones de orden superior (funciones que reciben otras funciones).
estudiantes = [
    {"nombre": "Ana", "edad": 22, "calif": 90},
    {"nombre": "Luis", "edad": 19, "calif": 85},
    {"nombre": "Sara", "edad": 25, "calif": 95}
]

# Si intentamos ordenar, falla o no hace lo que queremos
# print(sorted(estudiantes)) # Da error

# Usamos 'key=' para decirle CÓMO ordenar.
# 'key' espera una FUNCIÓN.
# Le pasamos una 'lambda' que toma un estudiante (x) y devuelve su edad.
ordenados_por_edad = sorted(estudiantes, key=lambda x: x["edad"])

print("--- Ordenados por Edad ---")
for est in ordenados_por_edad:
    print(est)
