
def sumar(a, b):
    print("La suma es:", a + b)
    return a + b

marca_celulares = ['Samsung', 'Apple', 'Huawei', 'Xiaomi', 'Motorola']
print("Todas las marca de celulares son: ")
print(marca_celulares)

# Vamos a eliminar a Apple
del marca_celulares[1]

print("Todas las marca de celulares son: ")
print(marca_celulares)

# esto es un metodo
marca_celulares.remove('Huawei')

print(marca_celulares)


# funcion
sumar(1,3)