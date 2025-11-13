#Metodo .read()
#! Para leer archivos es necesario que existan
with open("reporte.txt", "r") as f:
    contenido_total = f.read()
print(contenido_total)
#! ¡Peligro! Si el archivo es un log de 2GB, ¡intentará meter 2GB de texto en una sola variable en tu RAM! 
#! No usar para archivos grandes.