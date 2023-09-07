


# return -> devuelve un valor y termina la ejecución de la función



def sumar( a, b ):
    total = a + b
    return total


nro_uno = input("Ingrese un número: ")
nro_uno = int(nro_uno)
nro_dos = input("Ingrese otro número: ")
nro_dos = int(nro_dos)


total = sumar(nro_uno, nro_dos)
print("La suma de los números es: ", total)