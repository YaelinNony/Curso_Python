#Clase vs objeto
#! Clase: es la plantilla que usamos para crear algo (o un plano)
    #? Un plano de un coche define que "un coche tendrá color, modelo y 4 ruedas".
    #? Una clase Estudiante define que "un estudiante tendrá nombre, id y calificaciones".
    #?La clase es la idea abstracta.
#! Objeto: s la cosa real que construyes a partir del plano.
    #? Un coche Tesla rojo (coche_ana) y un Ford azul (coche_luis) son dos objetos construidos con el mismo plano Coche.
    #? e1 (Ana Solis) y e2 (Luis Vega) son dos objetos construidos a partir de la clase Estudiante.
#! Podemos tener una sola clase y crear miles de objetos a partir de ellas

#! ¿Como se crea una clase?
#! Para definir una plantilla, usamos la palabra clave class. 
#! Por convención, los nombres de las clases siempre usan PascalCase (o UpperCamelCase), empezando con mayúscula.

# Sintaxis: class NombreDeLaClase:
class Estudiante:
    # 'pass' es un placeholder para indicar un bloque vacío
    pass
