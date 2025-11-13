#Sentencia de control IF
#La condicional if nos permite tomar decisiones de acuerdo a una condicion
#Para que la condicional funcione se requiere al menos una variable

#Programa que evalúa la temperatura de un reactor
temperatura_reactor = 105

#La primera regla: ¿supera el límite crítico?
if temperatura_reactor > 100:
    print("ALERTA! Temperatura critica. Activando sistema de enfriamiento.")
    print("... sistema de enfriamiento ativado.")
temperatura_reactor = int(input("Introduce la nueva temperatura del reactor: "))
print("La nueva temperatura del reactor es", temperatura_reactor)