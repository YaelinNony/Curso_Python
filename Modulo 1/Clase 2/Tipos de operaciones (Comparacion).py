#Comparaciones

x = 10
y = 20

print("Igualdad: ", x==y)
print("Desigualdad: ", x!=y)
print("Mayor que: ", x>y)
print("Menor que: ", x<y)

#Logicos

p = True
q = False

print("AND: ", p and q)
print("OR: ", p or q)
print("NOT: ", not q)

a = int(input("Dame un número: "))
b = int(input("Dame otro número: "))

print("La igualdad de {a} == {b} es: ", a==b)
print("La desigualdad de {a} != {b} es: ", a!=b)
print("La comparación {a} > {b} es: ",a>b)
print("La comparación {a} < {b} es: ",a<b)
print("El AND de {a} > 5 and {b} < 10 es: ", a>5 and b<10)
print("El OR de {a} > 5 or {b} < 10 es: ", a>5 or b<10)
print("El NOT de {a} > 5 es: ", not a>5)