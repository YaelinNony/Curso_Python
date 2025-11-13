#manipulando datos
class Coche:
    def __init__(self, color_del_coche, modelo_del_coche):
        print(f"Construyendo un coche {color_del_coche} modelo {modelo_del_coche}...")

# Ahora, al crear el objeto, pasamos los argumentos
# Python los recibe en __init__
# self -> mi_tesla
# color_del_coche -> "Rojo"
# modelo_del_coche -> "Model S"
mi_tesla = Coche("Rojo", "Model S")

# self -> mi_ford
# color_del_coche -> "Azul"
# modelo_del_coche -> "Mustang"
mi_ford = Coche("Azul", "Mustang")