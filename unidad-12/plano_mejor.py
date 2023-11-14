


# Plano mejor que anidado


sistemas = {}
sensores_sistema = {}
valores_sensor = {}
ajustar_valor = {}


# version anidada
valores_ajustados = []
for s in sistemas:
    sensores = sensores_sistema(s)
    for sensor in sensores:
        valores_s = valores_sensor(sensor)
        for val in valores_s:
            valores_ajustados.append(ajustar_valor(val))

# version aplanada pero densa
valores_ajustados = [ajustar_valor(val) for val in valores_sensor(sensor) for sensor in sensores_sistema(s) for s in sistemas]



# version en funciones simples, testeables y escalables

def valores_del_sistema_ajustados(sistemas):
    for sistema in sistemas:
        yield valores_sistema(sistema)

def valores_sistema(sistema):
    for sensores in sistema:
        yield valores_sensores(sensores)

def valores_sensores(sensores):
    for sensor in sensores:
        yield valores_sensor_ajustados(sensor)

def valores_sensor_ajustados(sensor):
    for valor in valores_sensor(sensor):
        yield ajustar_valor(valor)





# Disperso es mejor que denso..

# version densa
print(','.join(map(str, [x ** 2 for x in range(5)])))


# version dispersa
a = [x ** 2 for x in range(5)]
b = map(str, a)
c = ','.join(b)

print(c)

# La legibilidad cuenta
lista_de_cuadrados = [x ** 2 for x in range(5)]
cadenas_de_cuadrados = map(str, a)
cuadrados_formateados = ','.join(b)





