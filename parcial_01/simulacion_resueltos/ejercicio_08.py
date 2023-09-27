

"""
Vamos a crear dos listas, que tengan 6 elementos cada uno. Dado1 y Dado2.

Utilizando la libreria random, vamos a simular una tirada de los dos dados.

Y consultarle al usuario que numero quiere apostar.
Entonces el usuario responde con un numero del 1 al 6.
En caso de que haya salido una vez, gana 5 puntos. Caso de que haya salido dos veces gana 10 puntos.
Caso de que no haya salido en ningun de los dos dados, pierde 5 puntos.

Sigue tirando los dados hasta que el usuario supere los 30 o -30. Y en cada caso dice si gano o perdio.
Gana si supera los 30. Pierde si supera los -30.




"""

import random

def tirar_dado():
    """Nos devuelve un numero random del 1 al 6."""
    return random.choice([1, 2, 3, 4, 5, 6])

apostar_numero = 1
puntos_total = 0
while apostar_numero >= 1 and apostar_numero <= 6:
    dado_1 = tirar_dado()
    dado_2 = tirar_dado()
    print("Ya tiré los dados dentro de mi memoria....")
    apostar_numero = int(input("Ingrese un numero del 1 al 6 para apostar: "))
    print("Salieron los numeros: ", dado_1, " y ", dado_2, ".")
    if apostar_numero >= 1 and apostar_numero <= 6:
        if dado_1 == apostar_numero and dado_2 == apostar_numero:
            print("Adivinaste los dos números...Gano 10 puntos...")
            puntos_total += 10
        elif dado_1 == apostar_numero or dado_2 == apostar_numero:
            print("Adivinaste un solo dado. Gano 5 puntos...")
            puntos_total += 5
        else:
            print("No salió el número que dijiste... Perdio 5 puntos...")
            puntos_total -= 5
        print("Puntos totales: ", puntos_total)
        if puntos_total >= 30:
            print("Ganaste!")
            exit(0)
        elif puntos_total <= -30:
            print("Perdiste!")
            exit(0)
    else:
        print("Debe ingresar un numero del 1 al 6. Fin de la ejecución.")
        exit(1)
    print("---------------------------------------------------")
    print("---------------------------------------------------")
