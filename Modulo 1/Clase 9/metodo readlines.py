#metodo readlines
#! Lee el archivo completo y lo vuelca en una lista de strings, 
#! donde cada elemento es una línea (¡con su \n!).
#! ¡Mismo Peligro! Carga todo el archivo a la RAM.
with open("reporte.txt", "r") as f:
    lista_de_lineas = f.readlines()
print(lista_de_lineas)
