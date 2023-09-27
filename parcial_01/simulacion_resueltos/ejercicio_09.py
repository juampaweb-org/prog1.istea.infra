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

import funciones_matematicas as fm

print("Bienvenido al programa de calculos matematicos.")

print("Ingrese el numero de la operacion que desea realizar: ")
print("1. Calcular area del circulo.")
print("2. Calcular area del triangulo.")
print("3. Calcular area del cuadrado.")
print("4. Calcular area del rectangulo.")
print("5. Calcular promedio de notas.")
print("6. Salir.")

opcion = int(input("Ingrese el numero de la operacion que desea realizar: "))

while opcion >= 1 and opcion <= 5:
    if opcion == 1:
        resultado = fm.calcular_area_circulo()
        print("El area del circulo es: ", resultado)
    elif opcion == 2:
        resultado = fm.calcular_area_triangulo()
        print("El area del triangulo es: ", resultado)
    elif opcion == 3:
        resultado = fm.calcular_area_cuadrado()
        print("El area del cuadrado es: ", resultado)
    elif opcion == 4:
        resultado = fm.calcular_area_rectangulo()
        print("El area del rectangulo es: ", resultado)
    elif opcion == 5:
        resultado = fm.calcular_promedio_notas()
        print("El promedio de notas es: ", resultado)
    
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    break

