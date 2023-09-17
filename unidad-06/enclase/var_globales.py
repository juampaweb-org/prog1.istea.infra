

import random

auto = 'Ford'

modelo = '2020'

def get_marca_random():
    global modelo
    modelo = '2023 Para todos'
    print('Modelos de autos: ' + modelo)
    marcas = random.choices(['Ford', 'Chevrolet', 'Fiat', 'Peugeot', 'Renault'])
    return marcas


print(modelo)
print(get_marca_random())

# print("Modelo de auto por fuera de la función: " + modelo)

