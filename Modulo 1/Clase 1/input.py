#Formas de interactuar con el usuario
#Entrada y salida de datos
#función input
#Siempre devuelve un string

print("Hola usuario, por favor ingresa tu nombre:")
nombre = input()
print("Hola " + nombre + ", bienvenido a Python")

#Otra forma de usar input
nombre = input("Por favor, ingresa tu nombre:")
print("Hola " + nombre + ", bienvenido a Python")


#función print
print("Hola usuario, por favor ingresa tu nombre:")
nombre = input()

#función print f
print(f"Hola {nombre}, bienvenido a Python")



#Si nosotros queremos que el usuario ingrese un número
#tenemos que convertir el string que devuelve input a número
edad = int(input("Por favor, ingresa tu edad: "))
print(f"Tu edad es {edad} años")