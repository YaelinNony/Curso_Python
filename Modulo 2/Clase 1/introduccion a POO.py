#introduccion a POO
#! En el modulo 1 escribimos código "procedural". Teníamos datos (en variables, listas, diccionarios) y funciones (def) que operaban sobre esos datos.
#! El Problema: Los datos y las funciones que los manipulan viven separados.
# Módulo 1: Datos y Funciones están separados
# --- El estilo del Módulo 1 ---
estudiante_1 = {
    "nombre": "Ana Solis",
    "id": "101",
    "calificaciones": []
}

estudiante_2 = {
    "nombre": "Luis Vega",
    "id": "102",
    "calificaciones": []
}

# Creamos funciones SUELTAS que RECIBEN el dato
def agregar_calificacion(estudiante, calif):
    # La función debe saber cómo están estructurados los datos
    estudiante["calificaciones"].append(calif)
    
def mostrar_info(estudiante):
    print(f"ID: {estudiante['id']} | Nombre: {estudiante['nombre']}")

# --- Uso ---
agregar_calificacion(estudiante_1, 9.5)
mostrar_info(estudiante_1)
#! Aquí, la base_de_datos es "tonta". Las funciones son las "listas" que la modifican. Esto se vuelve caótico en proyectos grandes

#? Si implementamos POO, podemos crear "cajas" personalizadas llamadas Objetos que son "inteligentes". 
#? Un objeto contiene sus propios datos (atributos) y sus propias funciones (métodos).
#! En lugar de tener una función que registra un alumno, tendremos un objeto SistemaAcademico que sabe cómo registrarse a sí mismo.
 