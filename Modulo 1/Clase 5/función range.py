#funcion range

print("Iniciando prueba de 5 ciclos del motor:")
# 'i' (de índice) es el nombre estándar para contadores
for i in range(5):
    print(f"Ciclo de prueba número {i+1}") 
# Usamos i+1 para que cuente 1, 2, 3, 4, 5
#si nosotros queremos un rango en especifico, podemos indicarlo en la funcion range
print("\nProbando ciclos del motor del 3 al 7:")
for i in range(3, 8):
    print(f"Ciclo de prueba número {i}")
#tambien podemos indicar un paso diferente a 1
print("\nProbando ciclos del motor del 2 al 10, de 2 en 2:")
for i in range(2, 12, 2):
    print(f"Ciclo de prueba número {i}")
# La función range puede tomar hasta tres argumentos: start, stop, step
#donde start es el valor inicial (incluido), stop es el valor final (excluido) y step es el incremento entre cada valor
# Queremos probar de 10 a 50 grados, de 10 en 10.
# range(inicio, fin_excluyente, pasos)
print("\nIniciando barrido de temperaturas:")
for temperatura in range(10, 51, 10): # 51 para que SÍ incluya el 50
    print(f"  - Realizando prueba de estrés a {temperatura}°C...")