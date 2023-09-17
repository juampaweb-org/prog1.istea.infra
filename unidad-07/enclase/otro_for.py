
# esta es una opcion
numeros = [1,3,4,2, 10]
len_numeros = len(numeros)
total = 0
for i in range(len_numeros):
    total = total + numeros[i]

print("La suma de los numeros es: ", total)

# Hay otra opción mejor.
numeros = [1,3,4,2, 10]
total = 0
for i in numeros:
    total = total + i
print("La suma de los numeros es: ", total)