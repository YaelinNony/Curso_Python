#Solucion usando setters y getters
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