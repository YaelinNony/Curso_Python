#Solucion usando setters
class ProductoSeguro:
    def __init__(self, nombre, precio_inicial):
        """Constructor del Producto Seguro"""
        self.nombre = nombre # El nombre puede ser público
        
        # 1. ATRIBUTO PRIVADO
        # Definimos el atributo privado con un valor "seguro" por defecto.
        self.__precio = 0.0 
        
        # 2. USANDO EL SETTER EN EL CONSTRUCTOR
        # En lugar de asignar 'precio_inicial' directamente,
        # usamos nuestro PROPIO método 'set_precio' para
        # validar el valor inicial.
        self.set_precio(precio_inicial) 

    # --- MÉTODO SETTER (El Cajero/Guardián) ---
    def set_precio(self, nuevo_precio):
        """
        Este es el método 'Setter' para el precio.
        Valida el 'nuevo_precio' antes de asignarlo.
        """
        print(f"-> Intento de asignar precio: {nuevo_precio}")
        
        # 3. VALIDACIÓN
        try:
            precio_num = float(nuevo_precio)
            
            if precio_num >= 0:
                # 5. ASIGNACIÓN SEGURA
                # Si todo es válido, se actualiza el atributo PRIVADO.
                self.__precio = precio_num
                print(f"✅ Precio actualizado a: ${self.__precio}")
            else:
                # 6. RECHAZO
                print(f"❌ Error: El precio '{precio_num}' no puede ser negativo.")
                
        except ValueError:
            # 6. RECHAZO
            print(f"❌ Error: '{nuevo_precio}' no es un número válido.")
            
    # --- MÉTODO GETTER (Para leer el dato) ---
    def get_precio(self):
        """
        Este es el 'Getter'. Nos permite LEER el valor privado
        de forma segura.
        """
        return self.__precio

    def mostrar(self):
        print(f"Producto: {self.nombre}, Precio: ${self.__precio}")

# --- DEMOSTRACIÓN ---
# 1. Creación (Pasa por el Setter)
print("--- Creando producto A ---")
p1 = ProductoSeguro("Laptop", 1500) # El 1500 pasa por el setter
p1.mostrar()
print("\n--- Creando producto B (inválido) ---")
p2 = ProductoSeguro("Teclado", -50) # El -50 es rechazado por el setter
p2.mostrar() # Mostrará el valor por defecto (0.0)
# 2. Intentando Modificar (Set)
print("\n--- Modificando producto A ---")
p1.set_precio(2000.50) # Intento Válido
p1.set_precio("Trescientos") # Intento Inválido (ValueError)
p1.set_precio(-100) # Intento Inválido (Negativo)
# 3. Resultado Final
print("\n--- Resultado Final ---")
print(f"El precio final de {p1.nombre} es: ${p1.get_precio()}")