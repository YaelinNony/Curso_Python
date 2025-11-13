#Reto del día 4
lista_inicial = ["leche", "pan", "manzana"]
print("\t--- BIENVENIDO OwO ---")
print("-"*50)
print("\t--- MENÚ DE OPCIONES ---")
print("\t-> Añadir.")
print("\t-> Quitar.")
print("\t-> Revisar.")

eleccion = input("\nPor favor, escriba la opción requerida:")

if eleccion.lower() == "añadir":
    añadir_articulo = str(input("¿Qué desea añadir? "))
    lista_inicial.append(añadir_articulo)
    print("\nMODIFICACIÓN GUARDADA CON ÉXTIO :D")
    print("\nSu lista actual es: ", lista_inicial)
    print("\nVUELVA PRONTO :D")
elif eleccion.lower() == "quitar":
    quitar_articulo = str(input("¿Qué desea quitar? "))
    lista_inicial.remove(quitar_articulo)
    print("\nMODIFICACIÓN GUARDADA CON ÉXTIO :D")
    print("\nSu lista actual es: ", lista_inicial)
    print("\nVUELVA PRONTO :D")
elif eleccion.lower() == "revisar":
    print(f"Los artículos en su lista son:\n {lista_inicial}")
    print("\nVUELVA PRONTO :D")
else:
    print("Opción inválida :c vuelva a intentarlo")