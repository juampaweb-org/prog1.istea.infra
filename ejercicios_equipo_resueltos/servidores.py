





"""
Vamos a armar un diccionario de 100 servidores, en donde la clave va a ser el numero de servidor que va del 1 al 100,
y los valores por cada servidor, va a ser una lista, con (distro, ram, disco, ip, estado)
Los valores de distro son random entre: ubuntu, debian, centos, fedora, suse
Los valores de ram son random entre: 64, 128, 256 (en GB, pero ponemos el numero)
Los valores de disco son random entre: 1.92, 3.84, 7.68 (en TB, pero ponemos el numero)
Los valores de IP son 123.543.23.xxx (el xxx va desde 0 hasta 255)
Los valores de estado son: online, offline, warning, critical


La idea es en principio generar el diccionario, mostrarlo en pantalla,
y realizar diferentes funciones en donde pueda modificar los diferentes datos.
ejemplo -> modificar_distro(3, 'debian')   Le digo que el servidor 3, ahora tiene distro debian

Y otra función que me muestre el servidor que le pido:
mostrar_servidor(3)  -> me muestra el servidor 3, con todos sus datos


"""

import random

def obtener_ip_random():
    """Nos devuelve una ip aleatoria."""
    ip = "123.543.23."
    ip += str(random.randint(0, 255))
    return ip

def generar_servidores():
    """Genera un diccionario de 100 servidores."""
    servidores = {}
    for numero in range(1, 101):
        distro = random.choice(distros)
        ram_ = random.choice(ram)
        disco_ = random.choice(disco)
        ip = random.choice(ips)
        estado = random.choice(estados)
        servidores[numero] = [distro, ram_, disco_, ip, estado]
    return servidores

distros = ['ubuntu', 'debian', 'centos', 'fedora', 'suse']
ram = [64, 128, 256]
disco = [1.92, 3.84, 7.68]
estados = ['online', 'offline', 'warning', 'critical']

# ips = [obtener_ip_random() for _ in range(100)]
ips = []
for i in range(100):
    ips.append(obtener_ip_random())


servidor = generar_servidores()

# print(servidor)


def mostrar_servidor( nro_servidor ):
    """Muestra los datos de un servidor."""
    print("Datos del servidor: ", nro_servidor)
    print("Distro: ", servidor[nro_servidor][0])
    print("Ram: ", servidor[nro_servidor][1])
    print("Disco: ", servidor[nro_servidor][2])
    print("IP: ", servidor[nro_servidor][3])
    print("Estado: ", servidor[nro_servidor][4])

print("Mostramos el servidor 3")
mostrar_servidor(3)


