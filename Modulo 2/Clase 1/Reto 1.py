#RETO 1
#TODO Crear una clase (plantilla) llamada Componente que sirva como la ficha técnica para cualquier pieza en tu fábrica. Cada componente que
#TODO crees (cada objeto) debe ser inicializado con sus datos básicos y debe tener su propio historial de revisiones.

#* --------------------------------- Requisitos del Programa: ---------------------------------
# 
#? Definir la Clase:
#*                  Crea una clase llamada Componente (recuerda usar PascalCase, con la primera letra en mayúscula).
class Componente:
    
    def __init__(self, numero_serie, tipo_componente,costo): #? Crear el Constructor (__init__): Define el método constructor __init__.
#? Definir los Atributos: Dentro de __init__, debes "pegar" los argumentos al objeto (self) para crear sus atributos.
#*                  Creación de los atributos:
        self.serie = numero_serie
        self.componente = tipo_componente
        self.costo = costo

#? Integración (Módulo 1): También debes crear dos atributos por defecto dentro de __init__:      
        self.historial_revisiones = []
        self.esta_activo = True

#? Crear los Objetos (Instancias): Al final de tu script (fuera de la clase, al nivel principal), crea dos objetos (instancias) a partir de tu
#? clase Componente:
c1 = Componente("MTR-1001", "Motor", 550.75)
c2 = Componente("SNR-2050", "Sensor", 80.20)

#? Interactuar con los Atributos (Módulo 1):
#*                  Añade manualmente dos fechas (como strings) a la lista historial_revisiones del objeto c1 
#*                      (ej. c1.historial_revisiones.append("2025-10-25")).
c1.historial_revisiones.append("2025-10-30")
c1.historial_revisiones.append("2025-10-31")

#*                  Cambia el atributo esta_activo del objeto c2 a False.
c2.esta_activo = False

#? Imprimir un Reporte:
#*                  Imprime en la consola un reporte para cada objeto, accediendo directamente a sus atributos para mostrar toda su información: 
#*                  su S/N, tipo, costo, historial de revisiones y estado de actividad.

print(f"El componente con número de serie {c1.serie} es un {c1.componente}, con un costo de {c1.costo}.\nSe ha revisado en {c1.historial_revisiones} y se encuentra {c1.esta_activo}")
print(f"El componente con número de serie {c2.serie} es un {c2.componente}, con un costo de {c2.costo}.\nSe ha revisado en {c2.historial_revisiones} y se encuentra {c2.esta_activo}")
