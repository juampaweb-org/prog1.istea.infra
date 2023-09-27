"""

Generar dos listas diferentes con 20 numeros cada una aleatorios enteros que vayan desde 1 hasta 100.
Imprimir las dos listas.
Y luego realizar una lista de impares y otra de pares.

Imprimir las dos listas de impares y pares. Es decir los numeros de las dos listas aleatoria primeras,
pero separados en dos listas, una de pares y otra de impares.





"""

import random


lista_uno = []
lista_dos = []
for i in range(20):
    lista_uno.append(random.randrange(1, 100))
    lista_dos.append(random.randrange(1, 100))

print("Lista uno: ", lista_uno)
print("Lista dos: ", lista_dos)

lista_pares = []
lista_impares = []
for i in range(20):
    if lista_uno[i] % 2 == 0:
        lista_pares.append(lista_uno[i])
    else:
        lista_impares.append(lista_uno[i])
    # con la lista 2
    if lista_dos[i] % 2 == 0:
        lista_pares.append(lista_dos[i])
    else:
        lista_impares.append(lista_dos[i])


print("Lista pares: ", lista_pares)
print("Lista impares: ", lista_impares)
