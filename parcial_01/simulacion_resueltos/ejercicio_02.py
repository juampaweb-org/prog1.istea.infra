

"""
Escribir en pantalla las siguientes figuras utilizando operadores aritmeticos, y bucles for y/o while.

1. Cuadrado
+*********************+
*                     *
*                     *
*                     *
*                     *
*                     *
*                     *
*                     *
*                     *
+*********************+

2. Rectangulo
+*************************************+
*                                     *
*                                     *
*                                     *
*                                     *
+*************************************+

3. Triangulo

+
**
***
****
*****
******
*******
********
*********
**********
***********
************
*************


"""


# +*********************+
# *                     *
# *                     *
# *                     *
# *                     *
# *                     *
# *                     *
# *                     *
# *                     *
# +*********************+

print("1. Cuadrado")
for i in range(10):
    if i == 0 or i == 9:
        print("+" + "*" * 21 + "+")
    else:
        print("*" + " " * 21 + "*")

input("Presione enter para continuar...")

print("2. Rectangulo")
for i in range(5):
    if i == 0 or i == 4:
        print("+" + "*" * 37 + "+")
    else:
        print("*" + " " * 37 + "*")

input("Presione enter para continuar...")

print("3. Triangulo")
for i in range(13):
    if i == 0:
        print("+")
    else:
        print("*" * i)

