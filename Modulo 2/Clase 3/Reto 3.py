# Reto 3: Diseñar un sistema de clases que utilice Herencia para modelar la flota. 
# Debes crear una clase Padre genérica (Vehiculo) y dos clases Hijas (Coche y Camion).


# CLASE PADRE: Vehículo
class vehiculo: 
# Constructor (__init__) que acepta marca, modelo y anio.
    def __init__(self,marca, modelo, anio):
        # Atributos:
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
        self._encendido = False
    
    #Métodos públicos
    def arrancar(self):
        if not self._encendido:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado")
        else:
            print(f"El el vehículo ya estaba en marcha.")
            
    def apagar(self):
        if self._encendido:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado")
    
    def get_kilometraje(self):
        return self.kilometraje
    
    def mostrar_info_base(self):
        print(f"Marca:{self.marca}\nModelo: {self.modelo}\nAño: {self.anio}")

#CLASE HIJA: Coche (Hereda de Vehiculo)
class Coche(vehiculo):
#Constructor (__init__) acepta marca, modelo, anio y también num_puertas.
    def __init__(self,marca,modelo,anio,num_puertas):
# Llamando al constructor de Padre inicializar la marca, modelo y año.
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas #Atributo
        
    def conducir(self, km): #Método
        if self._encendido: #Comprobar si self.encendido es True
            self.kilometraje += km
            print(f"Conduciendo {km} km...")
        else:
            print("Error: El coche debe estar arrancado para conducir.")

#CLASE HIJA: Camion (Hereda de Vehiculo)
class Camion(vehiculo):
# Constructor (__init__) acepta marca, modelo, anio y también capacidad_carga_kg.
    def __init__(self,marca,modelo,anio,capacidad_carga_kg):
# Llamando al constructor de Padre inicializar la marca, modelo y año.
        super().__init__(marca,modelo,anio)
# Atributos
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0
#Métodos
    def cargar(self,kilos):
        if self.__carga_actual_kg + kilos <= self.capacidad_carga_kg:
            self.__carga_actual_kg += kilos
            print("Carga exitosa.")
        else: 
            print("Error: Sobrecarga.")
    
    def descargar(self,kilos):
        if kilos <= self.__carga_actual_kg:
            self.__carga_actual_kg -= kilos
            print(f"Descarga exitosa")
        else:
            print("Error: No fue posible realizar la operación.")

    def get_carga_actual(self):
        return self.__carga_actual_kg


# Ejecución del Programa (El Código Principal):

#Creación del objeto mi_coche
mi_coche = Coche("Toyota", "Verde", 2008, 4)

#Creación del objeto mi_camion
mi_camion = Camion("Nissan","Azul",2016,5000)
print("Prueba del coche")
#Prueba del objeto coche
#Intentando conducir (Debe fallar)
mi_coche.conducir(10)
#Intentando arrancar
mi_coche.arrancar()
#Intentando conducir a 100 km
mi_coche.conducir(100)
#Intentando apagar
mi_coche.apagar()

print(f"El kilometraje es actual es: {mi_coche.get_kilometraje()} km/h")

print("\nPrueba del camión")
#Prueba del objeto camión
#Carga 3000 kg
mi_camion.cargar(3000)
#Intentando cargar debe fallar
mi_camion.cargar(3000)
#Intentando descargar
mi_camion.descargar(1000)

print(f"La carga actual es: {mi_camion.get_carga_actual()} kg")