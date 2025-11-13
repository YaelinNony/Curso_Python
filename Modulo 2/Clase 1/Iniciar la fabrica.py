#Iniciar la fabrica
#! Nuestros objetos e1 y e2 están vacíos. Necesitamos una forma de darles sus datos (nombre, id) en el momento en que son creados.
#! Para esto usamos un método "mágico" (o "dunder") llamado __init__.
#? este es un CONSTRUCTOR
#? La cual se ejecuta automaticamente cada vez que creas un nuevo objeto de esa clase.
class Estudiante:    
    # El Constructor
    def __init__(self):
        print("¡OBJETO CREADO! La fábrica __init__ está trabajando...")
print("Creando el primer estudiante...")
e1 = Estudiante() # Esto llamará a __init__
print("Creando el segundo estudiante...")
e2 = Estudiante() # Esto llamará a __init__ de nuevo

#!¿Por que usar self?
#? pones self porque es la forma en que el objeto que estás creando se refiere a sí mismo.
#? self es la variable que te permite guardar datos dentro del objeto.

