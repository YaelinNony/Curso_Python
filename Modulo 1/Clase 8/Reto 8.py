#Reto 8.
# Crear un programa que actúe como control de calidad de una fábrica de componentes, para registrar y evaluar las piezas que salen de la línea
# de producción. El programa debe ser 100% modular (usando funciones) y robusto (no puede "crashear" por entradas de usuario incorrectas).

#! Ejecutar Acciones (Manejo de Errores Obligatorio):
#?                      REGISTRAR:
#TODO                  -> Pide un Número de Serie (S/N).
#TODO                  -> Pide el nombre del componente (tiene que ser un componente válido de la tupla antes creada)
#TODO                  -> Pide 3 resultados de pruebas (0-100).
#TODO                  -> Crea el diccionario anidado para la nueva pieza (con estado "Pendiente") y añádelo a base_de_partes usando su S/N como clave.
#?                      BUSCAR:
#TODO                  -> Pide un S/N.
#TODO                  -> Busca el S/N en base_de_partes.
#TODO                  -> Si lo encuentra, imprime todos sus datos (tipo, resultados y estado).
#TODO                  -> Si no lo encuentra, informa al usuario con un mensaje de error claro
#?                      EVALUAR:
#TODO                  -> Pide un S/N.
#TODO                  -> Busca la pieza.
#TODO                  -> Calcula el promedio de los 3 valores en su lista resultados_pruebas.
#TODO                  -> Si el promedio es mayor o igual a 90.0, cambia el "estado" de la pieza a "Aprobado".
#TODO                  -> Si es menor, cámbialo a "Rechazado".
#TODO                  -> Imprime un mensaje confirmando la evaluación y el nuevo estado.
#?                      VER_INVENTARIO:
#TODO                  -> Imprime una línea resumen por cada pieza, mostrando: S/N: [ID] - Tipo: [Tipo] - Estado: [Estado].
#?                      CONTEO:
#TODO                  -> Pide al usuario un tipo_componente para buscar (ej: "Motor").
#TODO                  -> Debes crear una función recursiva (que se llame a sí misma). Esta función no puede usar bucles for o while.
#TODO                  -> La función debe recibir la lista de todas las piezas (puedes pasar list(base_de_partes.values())) y el tipo a contar.
#TODO                  -> Debe devolver el número total de piezas que coinciden con ese tipo.
#?                      SALIR:
#TODO                  -> Debe imprimir un mensaje de despedida (ej: "Cerrando sistema de QC...") y terminar el programa.

#* Estructura de datos inicial:
#TODO El programa debe empezar con un diccionario principal vacío llamado base_de_partes = {}.
base_de_partes = {}

#TODO La estructura para guardar cada pieza será un diccionario anidado dentro de base_de_partes. La clave será el Número de Serie (un string, ej: "SN-1001") y el valor serásdc
#TODO otro diccionario con los siguientes datos:

#? "tipo_componente": (Un string del tipo de parte).
#? "resultados_pruebas": (Una lista de 3 números flotantes).
#? "estado": (Un string, que iniciará como "Pendiente").

#TODO Debes crear una tupla global llamada COMPONENTES_VALIDOS que contenga los únicos tipos permitidos (ej: "Motor", "Sensor", "Batería", "Chasis").
componentes_validos = ('Motor', 'Sensor', 'Batería', 'Chasis')

#! Modularidad (Requisito Obligatorio): 
#TODO Todo tu programa debe estar construido con funciones. El bucle principal debe estar limpio y solo debe contener el menú y las llamadas
#TODO a las funciones que hacen el trabajo (ej: registrar_parte(), buscar_parte(), etc.). 
#! Está prohibido poner la lógica de registro o búsqueda directamente en el bucle principal.

#* FUNCIONES UTILIZADAS

#?                      REGISTRAR:
def registrar():
    print("CARGANDO...\n", "Se ha seleccionado la opción de manera exitosa")
    print("-"*45)

#TODO -> Pide un Número de Serie (S/N).
    try:
        registrar = int(input("Ingrese el número de serie (S/N). Debe ser un número entero:"))
        num_serie= "SN-"+ str(registrar)
    except ValueError:
        print("Valor no válido, intente de nuevo.")

    print(f"\nBuscando en la base de datos.")
    comprobar= base_de_partes.get(num_serie,"None")
    try:
        if comprobar == "None":
            partes = {"tipo_componente": " ","resultados_pruebas": [1,2,3],"estado": "Pendiente"}
#TODO -> Pide el nombre del componente (tiene que ser un componente válido de la tupla antes creada).
            partes["tipo_componente"]=input("Ingrese el nombre del componente: ")
            for componente in componentes_validos:
                if componente == partes["tipo_componente"]:
                    i=0
                    for resultados in partes["resultados_pruebas"]:
#TODO                  -> Pide 3 resultados de pruebas (0-100).
                        partes["resultados_pruebas"][i] = int(input(f"Ingrese el resultado de la prueba {i+1} (0-100): "))
                        i+=1
                else:
                    continue 
#TODO -> Crea el diccionario anidado para la nueva pieza (con estado "Pendiente") y añádelo a base_de_partes usando su S/N como clave.
            base_de_partes[num_serie] = partes
                    
    except Exception:
        print("ERROR: El número de serie ya se encuentra asociado a una parte. ")

def buscar():
    print("CARGANDO...\n", "Se ha seleccionado la opción de manera exitosa")
    print("-"*45)

#TODO -> Pide un Número de Serie (S/N).
    try:
        num_serie = int(input("Ingrese el número de serie (S/N). Debe ser un número entero:"))
        buscar= "SN-"+ str(num_serie)
    except IndexError:
        print("Valor no válido, intente de nuevo.")

    print(f"\nBuscando en la base de datos.")
    comprobar= base_de_partes.get(buscar,"None")
    try:
        if comprobar == "None":
            print("ERROR: Número de serie (S/N) no encontrado.")
        else:
            print(f"El SN corresponde a la parte: {base_de_partes[buscar]}")    
    except Exception:
        print("Ha ocurrido un error inesperado :c")

def evaluar ():
    print("CARGANDO...\n", "Se ha seleccionado la opción de manera exitosa")
    print("-"*45)
    
#TODO -> Pide un Número de Serie (S/N).
    try:
        num_serie = int(input("Ingrese el número de serie (S/N). Debe ser un número entero:"))
    except ValueError:
        print("Valor no válido, intente de nuevo.")

    promedio= "SN-"+ str(num_serie)
    print(f"\nBuscando en la base de datos.")
    comprobar= base_de_partes.get(promedio,"None")
    if comprobar != "None":
        print(f"El SN corresponde a la parte: {base_de_partes[promedio]["tipo_componente"]}")
        suma_prom = 0.0
        for calif in base_de_partes[promedio]["resultados_pruebas"]:
            suma_prom = suma_prom + calif
        cantidad_pruebas = len(base_de_partes[promedio]["resultados_pruebas"])
        prom = suma_prom / cantidad_pruebas
        if prom >= 90.0:
            base_de_partes[promedio]["estado"] = "Aprobado"
        elif prom < 90.0:
            base_de_partes[promedio]["estado"] = "Rechazado"
        
    elif comprobar == "None":
        print("ERROR: Número de serie (S/N) no encontrado.")
#? Intenté poner el "continue" en el if, pero me marcaba un error :c

def ver_inventario():
    print("CARGANDO...\n", "Se ha seleccionado la opción de manera exitosa")
    print("-"*45)
    
    for user_id, user_info in base_de_partes.items(): 
            print(f"S/N: {user_id}")
            for clave, valor in user_info.items():
                print(f"{clave}: {valor}")
                
def conteo (piezas,tipo):
    
    if not piezas:
        return 0
    
    primera = piezas[0]
    comprobar = 1 if  primera["tipo_componente"].lower() == tipo() else 0
    
    return comprobar + conteo(piezas[1:],tipo)
    
def salir():
        print("CARGANDO...\n", "Se ha seleccionado la opción de manera exitosa")
        print("-"*45)
        print("SALIDA EXITOSA, REGRESE PRONTO :D")

#* Bucle Principal:
#TODO El programa debe ejecutarse en un bucle infinito que presente el menú de opciones repetidamente, permitiendo al usuario realizar múltiples acciones.
try:
    while True:
        print("-"*45)
        print("\t BIENVENIDO")
        print("-"*45,"\n")
        #* Menú de Opciones:
    #TODO En cada ciclo, debe mostrar las opciones: "registrar", "buscar", "evaluar", "ver_inventario", "conteo" y "salir".
        print("*"*12, "Menú de opciones", "*"*12) 
        print("\n\t\t-> Registrar")
        print("\t\t-> Buscar")
        print("\t\t-> Evaluar")
        print("\t\t-> Ver inventario")
        print("\t\t-> Conteo")
        print("\t\t-> Salir")
        operacion = input("\nPor favor, introduzca una opción: ")

        if operacion.lower() == 'registrar': #* Si el usuario escribe "Registrar"
            registrar()
        if operacion.lower() == 'buscar': #* Si el usuario escribe "buscar"
            buscar()
        if operacion.lower() == 'evaluar': #* Si el usuario escribe "promedio"
            evaluar()
        if operacion.lower() == 'ver inventario': #* Si el usuario escribe "ver todos"
            ver_inventario()
        if operacion.lower() == 'conteo': #* Si el usuario escribe "ver todos"
            pieza = input("Escriba un componente para buscar: ")
            lista=list(base_de_partes.values())
            resultado = conteo(lista,pieza)
            print(f"Hay {resultado} piezas del tipo '{pieza}'.")
        if operacion.lower() == 'salir': #* Si el usuario escribe "salir"
            salir()
            break

except IndexError:
    print("Opción no encontrada, por favor, intente de nuevo c:")

#No entendí la parte del conteo :c 