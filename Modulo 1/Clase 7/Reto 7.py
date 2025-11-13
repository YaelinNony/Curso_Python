#Reto 7: crear un programa interactivo para administrar los datos de los estudiantes de un curso. 
#! El programa debe ejecutarse continuamente, debe ser robusta (no puede "crashear" por entradas incorrectas) y debe manejar una estructura de datos compleja: 
#! un diccionario de diccionarios.

 #! Requisitos del Programa:  

# TODO: 1) Estructura de Datos Inicial: El programa debe empezar con un diccionario principal vacío. La estructura para guardar a cada alumno será un diccionario anidado 
# TODO:                                 dentro de del diccionario, donde la clave es el ID del alumno (un string) y el valor es otro diccionario con sus datos, 
# todo                                  es decir, un diccionario anidado.
#?  Crear una tupla con materias válidas ("Resistencia de los materiales", "Control clásico", "Programación avanzada"), etc.
# TODO: 2) Bucle principal: El programa debe ejecutarse en un bucle infinito que presente el menú de opciones repetidamente, permitiendo al usuario realizar múltiples acciones.
# TODO: 3) Menú de opciones: En cada ciclo, debe mostrar las opciones: "registrar", "buscar", "promedio", "ver_todos", "cursos_unicos" y "salir"
# TODO: 4) Ejecutar acciones: 
#*                            Registrar: Pide un ID de alumno (ej. "103"). Comprueba si el ID ya existe en el diccionario. Si existe, muestra un error y vuelve al menú.
#*                            Pide el nombre del alumno.
#*                            Pide una materia. Obliga al usuario  a introducir una materia que esté in la tupla materias_validad
#*                            Pide 3 calificaciones. Asegurar que el usuario solo introduzca números. Guarda estas 3 calificaciones en una lista temporal.
#*                            Crea el diccionario anidado del nuevo alumno y añádelo al diccionario principal usando su ID como clave.
#*                            Buscar: Pide un ID de alumno. Busca al alumno. Si lo encuentra, imprime el nombre del alumno y su lista de calificaciones.
#*                            Promedio: Pide un ID de alumno. Obtén la lista de calificaciones del alumno Calcular el promedio de esa lista e imprímelo en pantalla.
#*                            Ver_todos: Imprime el ID y el nombre de cada alumno.    
#*                            Salir: Debe terminar el programa con un mensaje de despedida

#* Diccionario principal
base_de_datos = {}
#* Tupla con las materias válidas
materias_validas = ('Cálculo integral', 'Cálculo vectorial', 'Resistencia de los materiales', 'Control clásico', 'Programación avanzada', 'Control de máquinas eléctricas', 'Proyecto integrador')
suma_calif = 0.0 # Suma de calificaciones

#* Bucle principal
while True:
    print("-"*45)
    print("\t BIENVENIDO, DOCENTE :D")
    print("-"*45,"\n")
    print("*"*12, "Menú de opciones", "*"*12) #* Menú de Opciones
    print("\n\t\t-> Registrar")
    print("\t\t-> Buscar")
    print("\t\t-> Promedio")
    print("\t\t-> Ver todos")
    print("\t\t-> Salir")
    operacion = input("\nPor favor, introduzca una opción: ")

    if operacion.lower() == 'registrar': #* Si el usuario escribe "Registrar"
        
#*                            Registrar: Pide un ID de alumno (ej. "103"). Comprueba si el ID ya existe en el diccionario. Si existe, muestra un error y vuelve al menú.
        print("Cargando...\n", "Ha seleccionado la opción REGISTRAR con éxito.")
        print("-"*45)
        registrar = input("Ingrese el ID del alumno a registrar: ")
        print(f"\nBuscando en la base de datos.")
        comprobar= base_de_datos.get(registrar,"None")
        try:
            if comprobar == "None":
                alumno = {"nombre": " ","materia": 25,"calificaciones": [1,2,3]}
                #*                            Pide el nombre del alumno.
                alumno["nombre"]=input("Ingrese el nombre del alumno: ")
        except Exception:
            print("ERROR: El alumno ya se encuentra registrado. ")
            continue
        
        #* Pide una materia. Obliga al usuario  a introducir una materia que esté en la tupla materias_validas
        alumno["materia"]=input("Ingrese el nombre de la materia a registrar: ")
                
        for materia in materias_validas:
            if materia == alumno["materia"]:
                i=0
                for calificaciones in alumno["calificaciones"]:
                    #Pide 3 calificaciones. Asegurar que el usuario solo introduzca números. Guarda estas 3 calificaciones en una lista temporal.
                    alumno["calificaciones"][i] = int(input(f"Ingrese la calificacion {i+1}: "))
                    i+=1
        base_de_datos[registrar] = alumno
        
    if operacion.lower() == 'buscar': #* Si el usuario escribe "buscar"
        #Pide un ID de alumno. Busca al alumno. Si lo encuentra, imprime el nombre del alumno y su lista de calificaciones.
        print("Cargando...\n", "Ha seleccionado la opción BUSCAR con éxito.")
        print("-"*45)
        buscar = input("Ingrese el ID del alumno a buscar: ")
        print(f"\nBuscando en la base de datos.")
        comprobar= base_de_datos.get(buscar,"None")
        if comprobar == "None":
            print("ID del alumno no encontrado.")
        else:
            print(f"El ID corresponde al alumno: {base_de_datos[buscar]["nombre"]}")    
    
    if operacion.lower() == 'promedio': #* Si el usuario escribe "promedio"
        # Pide un ID de alumno. Obtén la lista de calificaciones del alumno Calcular el promedio de esa lista e imprímelo en pantalla.
        print("Cargando...\n", "Ha seleccionado la opción PROMEDIO con éxito.")
        print("-"*45)
        buscar_promedio = input("Ingrese el ID del alumno a realizar el promedio: ")
        print(f"\nBuscando en la base de datos.")
        comprobar= base_de_datos.get(buscar_promedio,"None")
        
        if comprobar == "None":
            print("ID del alumno no encontrado.")
        else:
            print(f"ID encontrado, calculando el promedio... ")
            
        for calif in base_de_datos[buscar_promedio]["calificaciones"]:
            suma_calif = suma_calif + calif
        
        cantidad_calif = len(base_de_datos[buscar_promedio]["calificaciones"])
        promedio = suma_calif / cantidad_calif
        print(f"El promedio del alumno es: {promedio:.2f}")
    
    if operacion.lower() == 'ver todos': #* Si el usuario escribe "ver todos"
        print("Cargando...\n", "Ha seleccionado la opción VER TODOS con éxito.")
        print("-"*45)
        for user_id, user_info in base_de_datos.items(): 
            print(f"ID de Usuario: {user_id}")
            for clave, valor in user_info.items():
                print(f"  {clave}: {valor}")
    
    if operacion.lower() == 'salir': #* Si el usuario escribe "salir"
        print("Cargando...\n", "Ha seleccionado la opción SALIR con éxito.")
        print("Programa finalizado, ¡regrese pronto! :D")
        break
