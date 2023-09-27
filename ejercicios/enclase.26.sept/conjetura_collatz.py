
"""
Una conjetura es una afirmación que se cree que es cierta, pero que no se ha demostrado.
Hay una muy famosa en matemáticas que se llama conjetura de collatz.

La conjetura de collatz dice que dado un numero entero positivo, si es par, se divide por 2, y si es impar, se multiplica por 3 y se le suma 1.
Haciendo este calculo sucesivamente, eventualmente llegara a 1.
En absolutamente todos los casos de los numeros enteros positivos.
Vamos a comprobarlo.

Pregunta al usuario un numero entero positivo, y luego, aplica la conjetura de collatz, hasta llegar al número 1.
Muestra todos los numeros que se van obteniendo en el camino.
Y comprueba que efectivamente, el ultimo numero que se obtiene es 1.
Y cuenta la cantidad de numeros que se obtuvieron en el camino.
Hasta el momento no se ha encontrado un numero que no cumpla esta conjetura, y aún no se puede demostrar que todos los numeros la cumplan.
"""



# 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# 100 -> 50 -> 25 -> 76 -> 38 -> 19 -> 58 -> 29 -> 88 -> 44 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

def calcular_siendo_par(numero):
        num_siguente = numero / 2
        return int(num_siguente)
def calcular_siendo_impar(nuemero):
        num_siguiente = nuemero * 3 + 1
        return int(num_siguiente)

lista = []
seguir = "s"
while seguir.lower() == "s":
    numero_ingresado = input("ingrese los números. Deben ser números enteros positivos.")

    while not numero_ingresado.isdigit():
        numero_ingresado = input("Ingrese NUMEROS. Deben ser ENTEROS POSITIVOS.")

    numero_actual = int(numero_ingresado)

    while numero_actual >= 1:
            if numero_actual == 1:
                lista.append(numero_actual)
                break
            elif numero_actual % 2 == 0:
                lista.append(numero_actual)
                numero_actual = calcular_siendo_par(numero_actual)
            else:
                lista.append(numero_actual)
                numero_actual = calcular_siendo_impar(numero_actual)

    print (lista)
    print ("hay" , len(lista), "numeros en la lista")

    seguir = input ("desea seguir S = si , N = no:  ")
    if seguir.lower() != "s" and seguir.lower() != "n" :
        seguir = input ("desea seguir S = si , N = no:  ")