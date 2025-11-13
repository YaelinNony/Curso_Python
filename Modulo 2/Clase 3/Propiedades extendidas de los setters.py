#Propiedades extendidas de los setters
#! Qué pasa si la Hija (ej. CuentaPremium) quiere modificar el comportamiento? 
#! No puede cambiar el __saldo, pero puede sobreescribir el método depositar() y luego llamar al método original del Padre usando super().
#? Aquí, la Hija añade su propia lógica (dar un bonus) antes de pasarle la responsabilidad al Padre.
# (La clase CuentaPadreSegura es la misma de arriba)
class CuentaPadreSegura:
    def __init__(self, saldo_inicial):
        # ATRIBUTO PRIVADO
        self.__saldo = 0.0
        
        # El Padre usa su PROPIO setter para validar el saldo inicial
        self.depositar(saldo_inicial)
    
    # --- SETTER PÚBLICO ---
    def depositar(self, cantidad):
        """
        El 'procedimiento oficial' para depositar.
        Es PÚBLICO y, por tanto, HEREDADO.
        """
        try:
            cantidad_num = float(cantidad)
            if cantidad_num > 0:
                self.__saldo += cantidad_num
                print(f"✅ (Padre) Depósito de ${cantidad_num} exitoso.")
            else:
                print("❌ (Padre) Error: Cantidad debe ser positiva.")
        except ValueError:
            print(f"❌ (Padre) Error: '{cantidad}' no es un número.")
            
    # --- GETTER PÚBLICO ---
    def get_saldo(self):
        """
        El 'procedimiento oficial' para leer el saldo.
        Es PÚBLICO y HEREDADO.
        """
        return self.__saldo

class CuentaHijaObediente(CuentaPadreSegura):
    def __init__(self, saldo_inicial):
        # Llama al __init__ del Padre (que a su vez llama a depositar())
        super().__init__(saldo_inicial)

    def realizar_deposito_hija(self, monto):
        print(f"\n-> (Hija) Intentando depositar {monto}...")
        
        # ¡ERROR! La Hija NO PUEDE tocar el atributo del Padre
        try:
            self.__saldo += monto # Esto fallará
        except AttributeError as e:
            print(f"   (Hija) ¡FALLO! No puedo acceder a __saldo. Error: {e}")
            
        # ¡FORMA CORRECTA! La Hija "sigue el procedimiento"
        # y llama al método PÚBLICO que SÍ heredó.
        print("   (Hija) Usando el método 'depositar()' del Padre...")
        self.depositar(monto)

# --- Uso ---
cuenta_hija = CuentaHijaObediente(1000)
print(f"Saldo inicial (leído con Getter): ${cuenta_hija.get_saldo()}")

cuenta_hija.realizar_deposito_hija(500)
cuenta_hija.realizar_deposito_hija("mil") # El setter del Padre lo validará

print(f"Saldo final (leído con Getter): ${cuenta_hija.get_saldo()}")
#iniciamos la extension de la hija
class CuentaPremium(CuentaPadreSegura):
    def __init__(self, saldo_inicial, bonus_tasa):
        super().__init__(saldo_inicial)
        self.__bonus_tasa = bonus_tasa # Atributo privado de la Hija
        print(f"¡Cuenta Premium creada con bonus de {bonus_tasa*100}%!")

    # --- SOBREESCRITURA DEL SETTER ---
    def depositar(self, cantidad):
        """
        La Hija sobreescribe el método 'depositar'
        para añadir su propia lógica PRIMERO.
        """
        print(f"\n-> (Hija Premium) Procesando depósito de ${cantidad}...")
        
        try:
            cantidad_num = float(cantidad)
            if cantidad_num <= 0:
                print("❌ (Hija) Error: Cantidad debe ser positiva.")
                return # Salimos de la función

            # 1. LÓGICA PROPIA DE LA HIJA
            bonus = cantidad_num * self.__bonus_tasa
            cantidad_total = cantidad_num + bonus
            print(f"   (Hija) Añadiendo bonus de ${bonus:.2f}.")
            print(f"   (Hija) Monto total a depositar: ${cantidad_total:.2f}")
            
            # 2. LLAMADA AL PADRE (super())
            # La Hija no toca __saldo. Llama al 'setter' del Padre
            # con el nuevo total para que él lo guarde de forma segura.
            super().depositar(cantidad_total)

        except ValueError:
            print(f"❌ (Hija) Error: '{cantidad}' no es un número.")

# --- Uso ---
cuenta_premium = CuentaPremium(1000, 0.10) # 10% de bonus
print(f"Saldo inicial: ${cuenta_premium.get_saldo()}")

cuenta_premium.depositar(500)
cuenta_premium.depositar(2000)

print(f"Saldo final Premium: ${cuenta_premium.get_saldo()}")