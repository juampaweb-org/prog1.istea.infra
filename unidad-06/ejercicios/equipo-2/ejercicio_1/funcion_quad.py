#Paso 3 Importamos modulo 'math'
import math

#Paso 4 
#Definimos Funcion calcular_raices
#Determinamos si discriminante es positivo, negativo o CERO, y hacemos return de cada caso

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c
   
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    elif discriminante == 0:
        x = -b / (2*a)

        return x
    else:
        return "Nada"