#ciclos de control for
#un bucle es una secuencia de instrucciones que se repiten hasta que una condicion deje 
# de cumplirse
#la sintaxis de un bucle for es:
secuencia = [1, 2, 3, 4, 5]
#¿Cual es la manera más facil de imprimir todos los elementos de una lista?
#La manera dificil:
print(secuencia[0])
print(secuencia[1])
print(secuencia[2])
print(secuencia[3])
print(secuencia[4])
#La manera facil:
for elemento in secuencia:
    print(elemento)
#la sintaxis del bucle for es:
#for variable in secuencia:
#como toda sentencia de control, lo que va dentro del bucle debe ir indentado
#podemos usar cualquier secuencia, como una cadena de texto