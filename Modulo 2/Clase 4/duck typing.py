#duck typing
#! "Si camina como un pato 🦆 y grazna como un pato 🦆... entonces es un pato."
#! A Python no le importa si los objetos heredan del mismo Padre. 
#!  Solo le importa si tienen el método que estás intentando llamar.

class Estudiante: # NO hereda de nadie
    def mostrar_info(self):
        print("Soy un ESTUDIANTE.")

class Profesor: # NO hereda de nadie
    def mostrar_info(self):
        print("Soy un PROFESOR.")

class ArchivoConfig: # NO hereda de nadie
    def mostrar_info(self):
        print("Soy un ARCHIVO DE CONFIGURACIÓN.")
        
class Coche:
    def arrancar(self):
        print("Vroom vroom!")
        
# --- El bucle polimórfico (Duck Typing) ---
# Mezclamos objetos que NO están relacionados
# pero que "graznan" igual (tienen .mostrar_info())
lista_cosas = [Estudiante(), Profesor(), ArchivoConfig()]

# ¡Este bucle FUNCIONA!
for item in lista_cosas:
    item.mostrar_info()
# ¿Qué pasa si añadimos el coche?
# lista_cosas.append(Coche())
# for item in lista_cosas:
#    item.mostrar_info() # ¡Esto CRASHEARÍA! El Coche no "grazna"