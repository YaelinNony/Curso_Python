#Reto del día 5
#Crear un programa que automatice el análisis de las calificaciones de un curso. 
#El programa debe ser interactivo y permitir al profesor ingresar los datos de sus
#estudiantes para luego generar un reporte completo, el programa se debe de dividir
# en fases:

print("Bienvenido, profesor:\n")

# 1) Vamos a solicitar al usuario la cantidad de alumnos que vamos a registrar
num_alumnos = int(input("Introduce el número de alumnos a registrar: "))


# 2) Vamos a pedirle al usuario el nombre y la calificación de cada alumno, (Estas las
# vamos a guardar en listas, una para los nombres, y otra para las calificaciones)
nombres= []
calificaciones = []
for i in range(num_alumnos):    
    print(f"Ingrese los datos del alumno no. {i+1}")
    nombres.append(input("Nombre: ").capitalize())
    calificaciones.append(float(input("Calificación: ")))
    

# 3) Vamos a crear tres listas vacías (Aprobados, reprobados y excelentes)
aprobados = []
reprobados = []
excelentes = []

# 4) Vamos a calcular el promedio general del grupo
suma_calif = 0.0 # Suma de calificaciones
for calif in calificaciones:
    suma_calif = suma_calif + calif

cantidad_calif = len(calificaciones)
promedio = suma_calif / cantidad_calif

# 5) Clasificar a todos los alumnos de acuerdo a su calificación, y pasar su nombre a
#  su correspondiente lista.
# (Reprobados < 5, aprobados >6, excelentes =10)
n = 0
for clasificacion in calificaciones:
    if clasificacion < 5:
        alumno= nombres[n]
        reprobados.append(alumno)
    elif clasificacion > 6 and clasificacion<10:
        alumno= nombres[n]
        aprobados.append(alumno)
    else:
        alumno= nombres[n]
        excelentes.append(alumno)
    n+=1

# 6) Al final imprimir toda la información:
# Numero total de estudiantes
# Promedio del salón
# Calificación mas baja y  más alta
# Imprimir las listas de excelentes, aprobados y reprobados.

print(f"\n------  Reporte Final    ------")
print("-"*30)
print(f"Número de estudiantes: {num_alumnos}")
print(f"Promedio del salón: {promedio:.2f}")
print(f"Calificación más alta: {max(calificaciones):.2f}")
print(f"Calificación más baja: {min(calificaciones):.2f}")
print(f"Alumnos excelentes: {excelentes}")
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")
print("-"*30)