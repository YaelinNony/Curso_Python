#clases privadas
#! Es una fuerte advertencia. El programador te está diciendo: "Oye, este atributo es para uso interno de la clase. 
#! No lo toques directamente desde fuera, o podrías romper algo. Si necesitas interactuar con él, usa un método público (como un getter o setter)."

#! Siguiendo con la analogia del carro:
#? Es el tapón del aceite bajo el capó. Técnicamente puedes quitarlo, pero no deberías hacerlo mientras conduces. 
#? Se espera que lo uses solo en situaciones controladas (como un "método" de mantenimiento).

class Bateria:
    def __init__(self, capacidad):
        # ATRIBUTO PROTEGIDO
        self._capacidad = capacidad
        self._voltaje_actual = 0
    
    # MÉTODO PÚBLICO
    def cargar(self):
        # Este método SÍ puede modificar los protegidos
        self._voltaje_actual = self._capacidad
        print(f"Batería cargada a {self._voltaje_actual}V")

mi_bateria = Bateria(12)
mi_bateria.cargar()

# Puedes "hacer trampa" y tocarlo, pero no deberías.
# Si lo haces, es bajo tu propio riesgo.
mi_bateria._voltaje_actual = -100 
print(f"Voltaje corrupto: {mi_bateria._voltaje_actual}")