'''
INSTRUCCIONES: Realiza un programa que le pida los siguientes datos al usuario y los imprima dato por dato:

•Nombre (str)
•Edad (int)
•Frase favorita (str)
•Cantidad de dinero disponible (float)

•Extra: realiza un mensaje personalizado donde se impriman todos los
datos en conjunto

'''

print("Bienvenido, por favor introduzca su nombre:")
nombre = input()
print(f"Bienvenido {nombre}, por favor, responda las siguientes preguntas:)")
edad = int(input("¿Cuál es su edad? "))
print(f"Tu edad es {edad} años")
frase = input("¿Cuál es tu frase favorita? :) \n")
print(f"Así que tu frase favorita es: \"{frase}\"")
dinero = float(input("Última pregunta, lo prometo nwn, si no es mucha indiscreción, ¿cuál es tu candidad de dinero disponible?\n"))
print(f"Tu cantidad de dinero disponible es: ${dinero}")
print("Encuesta terminada, se mostrará una lista con la información proporcionada. :D \n")
print("\n")

print("********************************************")
print(f"Nombre: {nombre}.\n")
print(f"Edad: {edad} años.\n")
print(f"Frase favorita: {frase}.\n")
print(f"Cantidad de dinero disponible: {dinero} \n")
print("********************************************")
print("\n Gracias por participar, nos vemos luego OwO/")
print("\n")
