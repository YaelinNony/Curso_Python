#Uso de clases mas privadas
#! Los miembros privados NO SE HEREDAN!
    #? Como el nombre fue cambiado a _Padre__caja_fuerte, la clase Hija no sabe que existe.
    #? Si la Hija define su propio self.__caja_fuerte, Python lo renombrará a _Hija__caja_fuerte. Serán dos atributos completamente diferentes.
#! Para datos críticos que solo el Padre debe controlar. 
#! La única forma en que la Hija puede acceder a ellos es si el Padre le da un método público (un Getter) para hacerlo.

class Padre:
    def __init__(self):
        # Atributo PRIVADO
        self.__numero_cuenta = "123-456-PADRE"
    
    # Método PÚBLICO (Getter)
    def get_datos_bancarios(self):
        """
        Esta es la interfaz pública (el "permiso")
        para que los hijos puedan LEER el dato privado.
        """
        return self.__numero_cuenta
        
    # Método PRIVADO
    def __cobrar_impuestos(self):
        print("Cobrando impuestos del Padre...")

class Hija(Padre):
    def __init__(self):
        super().__init__()
        
        # 2. La Hija crea SU PROPIO atributo privado
        self.__numero_cuenta = "987-654-HIJA"

    def intentar_acceso_privado(self):
        print(f"Número de cuenta (Hija): {self.__numero_cuenta}")
        
        # 1. ERROR: Intento de acceder al privado del Padre
        try:
            # Esto busca self.__numero_cuenta (que es _Hija__numero_cuenta)
            # O busca self._Padre__numero_cuenta (que no sabe cómo)
            print(self.__numero_cuenta_padre) # No existe
        except AttributeError as e:
            print(f"ERROR al acceder al privado del Padre: {e}")

        # 3. FORMA CORRECTA: Usar el método PÚBLICO (Getter) del Padre
        print(f"Forma correcta (usando Getter): {self.get_datos_bancarios()}")
        
    def intentar_llamar_metodo_privado(self):
        try:
            self.__cobrar_impuestos() # ¡Falla!
        except AttributeError as e:
            print(f"ERROR al llamar al método privado del Padre: {e}")

# --- Uso ---
hija = Hija()
hija.intentar_acceso_privado()
hija.intentar_llamar_metodo_privado()

# 4. Acceso directo desde fuera (¡También falla!)
try:
    print(hija.__numero_cuenta)
except AttributeError as e:
    print(f"ERROR al acceder desde fuera: {e}")