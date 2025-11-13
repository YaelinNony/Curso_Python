#funciones recursivas
#! una funcion recursiva es aquella que se llama a sí misma
#! esta no es un tipo diferente de funcion, si no es una TECNICA o ESTILO de programación
#? Una función recursiva resuelve un problema dividiéndolo en una versión más pequeña del mismo problema.
#? Imaginemos una muñeca rusa (Matryoshka) 🪆
#? Para abrir la muñeca grande (el problema), debes abrir la muñeca mediana que está dentro (la llamada recursiva)
#? la cual te obliga a abrir la muñeca pequeña...
def factorial(n):
    # 1. Caso Base (la muñeca más pequeña)
    if n == 0 or n == 1:
        return 1
    # 2. Llamada Recursiva (abrir la siguiente muñeca)
    else:
        # El factorial de 'n' es n * (el factorial de n-1)
        return n * factorial(n - 1) 
# Así es como Python lo resuelve:
# factorial(4)
# -> 4 * factorial(3)
# -> 4 * (3 * factorial(2))
# -> 4 * (3 * (2 * factorial(1)))
# -> 4 * (3 * (2 * 1))
# -> 24
print(f"El factorial de 4 es: {factorial(3)}")
#! Toda función recursiva necesita un "Caso Base" (la muñeca más pequeña que ya no se puede abrir)
#! de lo contrario, se llamaría a sí misma infinitamente y causaría un error.