

import random


def obtener_ip_random():
    """Nos devuelve una ip aleatoria."""
    ip = "123.543.23."
    ip += str(random.randint(0, 255))
    return ip



distros = ['ubuntu', 'debian', 'centos', 'fedora', 'suse']
ram = [64, 128, 256]
disco = [1.92, 3.84, 7.68]
estados = ['online', 'offline', 'warning', 'critical']
# ips = [obtener_ip_random() for _ in range(100)]
ips = [] # creo lista vacia
for _ in range(100):
    ips.append(obtener_ip_random())


def generar_hash():
    """Genera un hash de 20 caracteres."""
    hash_ = ""
    for _ in range(20):
        hash_ += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    return hash_




def generar_servidores_hash():
    """Genera un diccionario de 100 servidores."""
    servidores_hash = {}
    for numero in range(1, 101):
        hash_ = generar_hash()
        servidores_hash[numero] = hash_
    return servidores_hash



def generar_valores_del_servidor():
    """Genera los valores del servidor."""
    distro = random.choice(distros)
    ram_ = random.choice(ram)
    disco_ = random.choice(disco)
    ip = random.choice(ips)
    estado = random.choice(estados)
    return [distro, ram_, disco_, ip, estado]



# Acá generamos el diccionario de servidores con el hash como clave
# ejemplo
# {
#     1: 'hjdhjwkjjshss',
#     2: 'hjdhjwkjjshsskj2',
# }
servidor = generar_servidores_hash()

servidores_hash = {}

for clave, valor in servidor.items():
    servidores_hash[valor] = generar_valores_del_servidor()




def mostrar_servidor( nro_servidor ):
    """Muestra los datos de un servidor."""
    hash = servidor[nro_servidor]
    print("El hash es: ", hash)
    print("Datos del servidor: ", nro_servidor)
    print("Distro: ", servidores_hash[hash][0])
    print("Ram: ", servidores_hash[hash][1])
    print("Disco: ", servidores_hash[hash][2])
    print("IP: ", servidores_hash[hash][3])
    print("Estado: ", servidores_hash[hash][4])
    print('----------------------------------------------')

def modificar_distro(nro_servidor, distro):
    """Actualiza la distro de un servidor."""
    hash = servidor[nro_servidor]
    servidores_hash[hash][0] = distro

def modificar_ram(nro_servidor, ram):
    """Actualiza la ram de un servidor."""
    hash = servidor[nro_servidor]
    servidores_hash[hash][1] = ram

