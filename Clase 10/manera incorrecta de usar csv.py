#manera incorrecta de usar csv
# CÓDIGO INCORRECTO
with open("reporte.csv", "r") as f:
    for linea in f:
        partes = linea.strip().split(',')
        print(partes)
