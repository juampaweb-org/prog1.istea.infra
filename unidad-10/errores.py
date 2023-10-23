





numero = input("Ingrese un numero: ")
numero_dos = input("Ingrese otro numero: ")

try:

    numero = int(numero)
    numero_dos = int(numero_dos)

    resultado = numero / numero_dos

    print("El resultado es: ", resultado)

except ValueError:
    print("Error en los valores...")

except ZeroDivisionError:
    print("No se puede dividir por cero...")

# ZeroDivisionError: division by zero
# ValueError: invalid literal for int() with base 10: 'fg'









