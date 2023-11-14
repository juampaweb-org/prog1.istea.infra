


import time as t

print("comienza el cronómetro")
tiempo_inicial = time.time()

print("detengo la ejecución por 4 segundos")
t.time.sleep(4)


tiempo_final = t.time.time()

delta_tiempo = tiempo_final - tiempo_inicial
print(" Pasaron ", delta_tiempo, " segundos")