#clases publicas
#! Python no tiene "clases privadas" o "clases públicas" de forma estricta. 
#! En Python, todas las clases son técnicamente públicas.

#! Cuando hablamos de "público" y "privado" en Python, nos referimos a qué tan accesibles son esos atributos y métodos desde fuera de la clase.
#? La filosofía de Python es: "Somos todos adultos aquí". 
#? En lugar de prohibir el acceso, Python usa una convención de nombrado (guiones bajos) para indicar la intención.

#! Los atributos o metodos sin guion bajo al inicio se consideran "publicos"
#! Se puede acceder y modificar libremente desde cualquier parte de tu código.
#? Imaginemos que son objetos creados para ser usados por el usuario en cualquier momento
#? Como un boton o una pantalla
#! Siguiendo la analogia del carro:
#? Son el volante, los pedales y el estéreo de un coche. 
#? Están hechos para que el conductor los use.
class Coche:
    def __init__(self, modelo):
        # Este atributo es PÚBLICO
        self.modelo = modelo
    
    # Este método es PÚBLICO
    def arrancar(self):
        print(f"El {self.modelo} ha arrancado.")

mi_coche = Coche("Tesla")
mi_coche.arrancar() # Puedes llamar al método
mi_coche.modelo = "Ford" # Puedes modificar el atributo
print(mi_coche.modelo)