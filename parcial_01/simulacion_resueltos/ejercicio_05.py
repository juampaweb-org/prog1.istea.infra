"""

Vamos a escribir los numeros de fibonacci.
Recordar que los numeros de finobacci son la suma de los dos anteriores.
ejemplo:
0,1,1,2,3,5,8,13.....

Vamos a pedirle al usuario que nos indique que cantidad de numeros de finobacci quiere ver.
Y vamos a imprimir en pantalla esa cantidad de numeros de finobacci.
Como máximo vamos a permitir que el usuario ingrese 40 numeros de finobacci.

"""


def calcular_finobaacci(cantidad_numeros):
    # excepción si el usuario elije ver un solo número
    if cantidad_numeros == 1:
        return [0]

    finobacci = [0]
    for i in finobacci:
        if i == 0:
            finobacci.append(1)
        else:
            nro_siguiente = finobacci[-2] + finobacci[-1]
            finobacci.append(nro_siguiente)
            if(len(finobacci) >= cantidad_numeros):
                break
    return finobacci


cant_numeros_user = int(input("Ingrese que cantidad de numeros de finobacci quiere ver: "))
finobacci = calcular_finobaacci(cant_numeros_user)
print("Los numeros de finobacci son: ")
print(finobacci)
