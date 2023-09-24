

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
    res1 = random.choice(dado1)
    #res2 = random.choice(dado2)   no se como dividir el resultado en 2 cuando llamo la funcion 
    return res1 #, res2 
    


puntos_total = 0
#dado1 = [1, 1, 2, 1, 2, 2] dado de pruebas
dado1 = [1, 2, 3, 4, 5, 6]
#dado2 = [1, 2, 3, 4, 5, 6] no entiendo porq 2 dados ni como hacer q 1 funcion me traiga los 2 y usarlos por separado


while puntos_total > -30 and puntos_total < 30:
    apuesta = input("que apuesta q sale ?:  ")
    while not apuesta.isdigit():
        apuesta = input("que NUMERO apuesta q sale ?:  ")
    else:
        while int(apuesta) < 1 or int(apuesta) > 6:
            apuesta = input("Del 1 al 6 amigo...:  ")
    apuesta = int(apuesta)
    
    resultado1 = tirar_dado()
    resultado2 = tirar_dado()
    print("salieron el: ", resultado1 , resultado2)

    if apuesta == resultado1 and apuesta == resultado2:
        puntos_total += 10
        print("le pegaste a ambos: sumas 10 puntos")
    elif apuesta == resultado1 or apuesta == resultado2:
        puntos_total += 5
        print("le pegaste a uno: sumas 5 puntos")
    elif apuesta != resultado1 and apuesta != resultado2:
        puntos_total -= 5
        print("no le pegaste: perdes 5 puntos")

    print("resultado parcial: ", puntos_total)
    print("-"*10)


if puntos_total <= -30:
   print("Buu Perdiste")
elif puntos_total >= 30:
   print("GANASTE!!!!!!!")