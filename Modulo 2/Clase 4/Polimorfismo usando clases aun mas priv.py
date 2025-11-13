#Polimorfismo usando clases aun mas privadas
#! Los métodos privados no pueden ser sobrescritos.
#! Cuando una clase Hija define un método con el mismo nombre __metodo_privado, no está sobrescribiendo, 
#! está creando un método completamente nuevo e independiente.
class Padre:
    def __init__(self):
        self.valor_padre = 10
    
    # --- MÉTODO PRIVADO DEL PADRE ---
    def __calcular(self):
        print(f"(Padre) Cálculo secreto con {self.valor_padre}")

    # Método público que LLAMA al privado
    def ejecutar(self):
        print("-> Padre ejecutando...")
        self.__calcular() # Llama a _Padre__calcular

class Hija(Padre):
    def __init__(self):
        super().__init__()
        self.valor_hija = 20
    
    # --- MÉTODO PRIVADO DE LA HIJA ---
    # Esto NO es una sobrescritura.
    # Python lo renombra a _Hija__calcular
    def __calcular(self):
        # ¡ERROR! ¡No podemos llamar al método del Padre!
        # super().__calcular() # <-- Esto daría AttributeError
        print(f"(Hija) Cálculo diferente con {self.valor_hija}")

    # Método público que LLAMA al privado
    def ejecutar(self):
        print("-> Hija ejecutando...")
        self.__calcular() # Llama a _Hija__calcular

# --- El Polimorfismo "Roto" ---
lista = [Padre(), Hija()]

print("--- Ejecutando polimorfismo aparente ---")
for obj in lista:
    # 1. Llamamos al método PÚBLICO 'ejecutar()'
    #    (Este SÍ es polimórfico)
    obj.ejecutar()