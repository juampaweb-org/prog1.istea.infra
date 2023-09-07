


import random


# choice(secuencia) -> devuelve un elemento aleatorio de la secuencia
# sample(secuencia, k) -> devuelve k elementos aleatorios de la secuencia



dado = [1, 2, 3, 4, 5, 6]

print("Tiramos el dado...")

print("Te salió el nro: ", random.choice(dado))


print("Tiramos el dado 10 veces...")
print(random.choices(dado, k=10))



