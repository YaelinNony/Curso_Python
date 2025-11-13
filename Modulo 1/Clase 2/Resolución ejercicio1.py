
#Se agregaron dos puntos más:
#1) Sumar 10 a la edad para saber qué edad tendría después de ese tiempo
#2) Si al dinero le diera 1000 mas, ¿cuánto dinero tendría?
nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
frase_favorita =  input("Dame tu frase favorita: ")
dinero = float(input("Cuánto dinero tienes?"))

print("Tu nombre es: ", nombre)
print("Tu edad es: ", edad)
print("Tu frase favorita es:", frase_favorita)
print("Tu dinero es: ", dinero)
print("En 10 años tendrás:", edad + 10)
print("Si te doy 1000 más, tendrás: ", dinero + 1000)
print(f"Hola {nombre}, tu frase favorita es '{frase_favorita}'. En 10 años tendrás {edad+10} y si te diera 1000 tendrás {dinero+1000}.")