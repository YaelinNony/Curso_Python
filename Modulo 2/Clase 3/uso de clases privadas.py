#uso de clases privadas

#! Tambien llamados atributos y metodos protegidos
#! Al igual que los públicos, los miembros protegidos son totalmente heredados y totalmente accesibles por la clase Hija.

#? El _ le dice a otros programadores (incluida la clase Hija): "Este miembro es para uso interno de la familia (Padre e Hijos). 
#? No deberías tocarlo desde fuera de la familia, pero si eres un Hijo y sabes lo que haces, puedes usarlo."
class Padre:
    def __init__(self):
        # Atributo PROTEGIDO
        self._receta_familiar = "Ingredientes: Harina, Huevos, Amor"
        
    # Método PROTEGIDO
    def _cocinar_base(self):
        print("Cocinando la base de la receta...")
        return "Base cocinada"

class Hija(Padre):
    def __init__(self):
        super().__init__()
    
    def crear_platillo_moderno(self):
        # 1. ACCESO VÁLIDO: La Hija (un miembro de la familia)
        #    PUEDE y DEBE usar los miembros protegidos del Padre.
        base = self._cocinar_base()
        
        # 2. ACCESO VÁLIDO: La Hija puede leer la receta.
        print(f"Usando la receta: '{self._receta_familiar}'")
        print(f"¡Platillo moderno creado sobre la '{base}'!")

# --- Uso ---
hija = Hija()
hija.crear_platillo_moderno()

# --- MALA PRÁCTICA (Aunque técnicamente funciona) ---
print("\n--- Acceso desde fuera (Mala Práctica) ---")
# Esto funciona, pero estás rompiendo la advertencia
hija._receta_familiar = "Ingredientes: Comida rápida" 
print(hija._receta_familiar)