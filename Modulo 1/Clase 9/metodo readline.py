#metodo readline
with open("reporte.txt", "r") as f:
    linea_1 = f.readline().strip() # .strip() quita el \n
    linea_2 = f.readline().strip()
print(f"La primera línea es: {linea_1}")
print(f"La segunda línea es: {linea_2}")