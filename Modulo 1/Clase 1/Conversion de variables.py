#Conversión de variables

a= 5
b = 2.5
c = "3"

print(a + b + int(c))

#podemos ver que la variable c es un string y no se puede sumar a las otras variables
#Por lo que convertimos c a entero con int()

print(a + b + float(c))
#Ahora convertimos c a flotar con float()

print(str(a) + str(b) + c)
#Ahora convertimos a y b en string con str()
#y los concatenamos en lugar de sumarlos

#Buenas prácticas al nombre variables

nombre_variable = "valor"
nombreVariable = "valor"

#NO se puede usar guión medio
#NO se puede usar espacios
#Las variables en python pueden contener letras, números y guión bajo
#pero no pueden empezar con un número
#y NO pueden contener caracteres especiales
