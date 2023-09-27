"""
Vamos a utilizar el modulo math, y a la vez crear un modulo personalizado de calculos matematicos.

En nuestro modulo, que lo debemos hacer en un archivo aparte, vamos a crear las siguientes funciones:
Las funciones deben estar documentadas con docstring. (detallo abajo)


1.calcular_area_circulo(radio)
2.calcular_area_triangulo(base, altura)
3.calcular_area_cuadrado(lado)
4.calcular_area_rectangulo(base, altura)
5.calcular_promedio_notas(notas)

El programa va a preguntar al usuario que desea hacer,
y en función de lo que el usuario elija, va a pedir los datos necesarios para calcular el area o el promedio de notas, etc,
etregando resultado y luego preguntando si desea hacer otra operación o salir del programa.

Formulas:
1. Area del circulo: pi * radio ** 2
2. Area del triangulo: (base * altura) / 2
3. Area del cuadrado: lado ** 2
4. Area del rectangulo: base * altura
5. Promedio de notas: sumatoria de notas / cantidad de notas

"""
import math


# Area circulo la función que lo realiza y la función que consulta al usuario.
def area_circulo(radio):
    """Calcula el area de un circulo"""
    return math.pi * radio ** 2

def calcular_area_circulo():
    """Calcula el area de un circulo"""
    radio = int(input("Ingrese el radio del circulo: "))
    return area_circulo(radio) 


## Area triangulo la función que lo realiza y la función que consulta al usuario.
def area_triangulo(base, altura):
    """Calcula el area de un triangulo"""
    return (base * altura) / 2

def calcular_area_triangulo():
    """Calcula el area de un triangulo"""
    base = int(input("Ingrese la base del triangulo: "))
    altura = int(input("Ingrese la altura del triangulo: "))
    return area_triangulo(base, altura)


# Area cuadrado la función que lo realiza y la función que consulta al usuario.
def area_cuadrado(lado):
    """Calcula el area de un cuadrado"""
    return lado ** 2

def calcular_area_cuadrado():
    """Calcula el area de un cuadrado"""
    lado = int(input("Ingrese el lado del cuadrado: "))
    return area_cuadrado(lado)


# Area rectangulo la función que lo realiza y la función que consulta al usuario.
def area_rectangulo(base, altura):
    """Calcula el area de un rectangulo"""
    return base * altura

def calcular_area_rectangulo():
    """Calcula el area de un rectangulo"""
    base = int(input("Ingrese la base del rectangulo: "))
    altura = int(input("Ingrese la altura del rectangulo: "))
    return area_rectangulo(base, altura)



# Promedio de NOTAS
def promedio_notas(notas):
    """Calcula el promedio de notas"""
    for nro in notas:
        if not nro.isdigit():
            return "Debe ingresar solo numeros"
    notas = [int(nota) for nota in notas]
    return sum(notas) / len(notas)

def calcular_promedio_notas():
    """Calcula el promedio de notas"""
    notas = input("Ingrese las notas separadas por coma: ")
    notas = notas.split(",")
    return promedio_notas(notas)


