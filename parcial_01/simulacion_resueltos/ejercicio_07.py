"""
Realizar un programa que le consulta al usuario cuantos numeros quiere ingresar. MAX 20 números, si pide más que 20 debe volver a preguntar avisandole que
puede poner 20 como máximo. Hasta que no ingrese menor que 20 no debe dejar de preguntar.

Luego una vez definido la cantidad de números que quiere ingresar, debe pedirle que ingrese los números. Deben ser números enteros positivos.
Los debe ir guardando en una lista.
Si el usuario ingresara un numero negativo o cero o string, debe volver a preguntarle que ingrese un número válido. (infinitas veces)
Una vez que los ingresó todos, debe imprimirlos en una sola línea separados por coma. Imprimir la lista de numeros ingresados.
Y luego debe hacer la suma de todos y mostrar el resultado en pantalla.

"""

numeros = []

cant_numeros_ingreso = input("Cuantos numeros desea ingresar?")

for i in range(int(cant_numeros_ingreso)):
    numero = input("Ingrese un numero: ")
    while not numero.isdigit():
        numero = input("Debe ingresar un numero entero positivo. Ingrese un numero: ")
    if numero.isdigit():
        numeros.append(int(numero))

print(numeros)
print("La suma de los numeros ingresados es: ", sum(numeros))
