# RETO 6: Crear un programa interactivo para gestionar el inventario de una estación 
# espacial.

#! El programa debe ser robusto: no puede "crashear" y debe ejecutarse continuamente 
#! hasta que el usuario decida salir.  

# *TODO Requisitos:
# *TODO     Bucle Principal: El programa debe ejecutarse en un bucle infinito que 
# *TODO                      presente el menú de opciones repetidamente, permitiendo 
# *TODO                      al usuario realizar múltiples acciones.
# *TODO     Lista Inicial: El programa debe empezar con una lista que ya contenga algunos 
# *TODO                    artículos.    
# *TODO     Menú de Opciones: En cada ciclo del bucle, debe mostrarle al usuario las 
# *TODO                       opciones disponibles: "añadir", "quitar", "ver",
# *TODO                       "inspeccionar" y "salir".
# *TODO     Ejecutar acciones:
# *TODO     > Si el usuario escribe "añadir": El programa le preguntará qué artículo
# *TODO       quiere añadir (ej. "paneles solares"). Lo agregará a la lista inventario.
# *TODO     > Si el usuario escribe "quitar": El programa le preguntará qué artículo 
# *TODO       quiere quitar. Debe comprobar primero si el artículo está en la lista. Si
# *TODO       está, lo elimina, si no está, debe informar al usuario: 
#*                   "Error: Ese ítem no existe en el inventario."        
# *TODO     > Si el usuario escribe "ver": Debe comprobar si la lista está vacía, si no 
# *TODO       lo está, imprimir la lista de manera ordenada
# *TODO     > Si el usuario escribe "inspeccionar": El programa preguntará: 
#*                   "¿Qué número de ítem quieres inspeccionar?".
# *TODO     > Si el usuario escribe "salir": El programa debe imprimir un mensaje de 
# *TODO       despedida y usar la sentencia break para detener el bucle while True:.
# *TODO     Informar el Resultado: Después de cada acción (añadir, quitar, inspeccionar),
# *TODO                            el programa debe mostrar un mensaje de confirmación y
# *TODO                            el estado actual de la lista inventario.


#* Lista Inicial
inventario = ["Comida", "Ropa", "Medicinas"]

#* Bucle principal
while True:
    print("-"*45)
    print("\t BIENVENIDO AL INVENTARIO :D")
    print("-"*45,"\n")
    print("*"*12, "Menú de operaciones", "*"*12) #* Menú de Opciones
    print("\n\t\t-> Añadir")
    print("\t\t-> Quitar")
    print("\t\t-> Ver")
    print("\t\t-> Inspeccionar")
    print("\t\t-> Salir")
    operacion = input("\nPor favor, introduzca una opción: ")
    
    if operacion.lower() == 'añadir': #* Si el usuario escribe "añadir"
        print("Cargando...\n", "Ha seleccionado la opción AÑADIR con éxito.")
        print("-"*45)
        art_añadir = input("¿Qué artículo desea añadir? ").capitalize()
        print(f"\nAñadiendo {art_añadir} al inventario, espere un momento...")
        
        try:
            inventario.append(art_añadir)
            print("¡El artículo ha sido añadido con éxito! :D")
            print(f"Su inventario actualizado es: \n{inventario}")
            print("-"*45,"\n")
            continue
        except Exception:
            print("¡A ocurrido un error inesperado D:")
            break

    if operacion.lower() == 'quitar': #* Si el usuario escribe "quitar"
        print("\tCargando...\n", "Ha seleccionado la opción QUITAR con éxito.")
        print("-"*45)
        art_quitar = input("¿Qué artículo desea quitar? ").capitalize()
        producto = inventario.count(art_quitar)
        
        try:
            if producto != 0:
                print(f"\nRetirando {art_quitar} al inventario, espere un momento...")
                inventario.remove(art_quitar)
                print("¡El artículo ha sido retirado con éxito! :D")
                print(f"Su inventario actualizado es: \n{inventario}")
                print("-"*45,"\n")
                continue
            print("Ese ítem no existe en el inventario. Debe introducir un producto en existencia.")
            continue
        except Exception:
            print("¡A ocurrido un error inesperado! D:")
            break
        
    
    if operacion.lower() == 'ver': #* Si el usuario escribe "ver"
        print("\tCargando...\n", "Ha seleccionado la opción VER con éxito.")
        print("-"*45)
        if len(inventario) > 0:
            inventario.sort()
            print(f"Su inventario actual es: {inventario}")
            print("-"*45)
            continue
        print("No tiene elementos en su inventario :c")
        print("-"*45)
        
    if operacion.lower() == 'inspeccionar': #* Si el usuario escribe "inspeccionar"
        print("\tCargando...\n", "Ha seleccionado la opción INSPECCIONAR con éxito.")
        print("-"*45)
        try:
            item = int(input("¿Qué número de item quieres inspeccionar? "))
            print(f"El item seleccionado es: {inventario[item]}")
            continue
        except ValueError:
            print("Error: Introduzca un número.")
        except IndexError: 
            print("Error: No existe un item en esa posicion.")
        
    if operacion.lower() == 'salir': #* Si el usuario escribe "salir"
        print("Programa finalizado, regrese pronto! :D")
        break 
        
