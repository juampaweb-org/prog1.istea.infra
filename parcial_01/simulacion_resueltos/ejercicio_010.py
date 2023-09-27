

"""
Vamos a simular que tenemos un script que negocia contra un servidor de IP xxx contra protocolo HTTP y el mismo hace devolución del código,
en función si hubo error, conectó bien, etc.

Seleccionar algunos de los códigos más importantes de la siguiente url:
https://kinsta.com/es/blog/codigos-de-estado-de-http/

Vamos primero a hacer un random de la conexión al servidor de la siguiente manera:
125.23.34.xxx -> el xxx va desde 0 hasta 255
y el mismo le devuelve codigo  del servidor.


Entonces lo primero que hacemos es determinar la ip del servidor, que es 125.23.34.xxx, utilizando random.

Luego consultamos al usuario si desea enviarle una petición al servidor 125.23.34.23 ?
Cuando le envia muestra mandando petición...

Y vamos a hacer una lista 5 de los diferentes codigos de respuesta.
En función del codigo de respuesta, vamos a mostrar un mensaje en pantalla, detallando lo que significa ese código

"""

import random
import time

def obtener_ip_random():
    """Nos devuelve una ip aleatoria."""
    ip = "125.23.34."
    ip += str(random.randint(0, 255))
    return ip

def mostrar_mensaje(codigo):
    """Muestra un mensaje en pantalla en función del codigo de respuesta."""
    if codigo == 200:
        mensaje = "Todo está bien"
    elif codigo == 301:
        mensaje = "El recurso solicitado ha sido trasladado permanentemente"
    elif codigo == 400:
        mensaje = "Mala petición"
    elif codigo == 501:
        mensaje = "No implementado"
    elif codigo == 508:
        mensaje = "Se ha alcanzado el límite de recursos"
    else:
        mensaje = "Codigo no reconocido"
    return mensaje

def desea_continuar():
    respuesta = input("Desea continuar? (s/n): ")
    if respuesta.lower() == "s":
        return True
    elif respuesta.lower() == "n":
        return False
    else:
        print("Respuesta invalida")
        return desea_continuar()



codigos_http = [200, 301, 400, 501, 508]


continuar = True

while continuar:
    print("La ip del servidor es: ", obtener_ip_random())
    print("Le estamos enviando una petición al servidor...")
    time.sleep(3)
    codigo_respuesta = random.choice(codigos_http)
    print("El codigo de respuesta es: ", codigo_respuesta)
    print("El mensaje es: ", mostrar_mensaje(codigo_respuesta))
    continuar = desea_continuar()
    if continuar == False:
        print("Fon de interacción con el servidor.")
        break


