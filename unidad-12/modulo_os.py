

import os


print("sistema Operativo: ", os.name)

# sistema_operativo = os.name



if sistema_operativo == 'posix':
    separadores_directorios = os.sep
elif sistema_operativo == 'nt':
    separadores_directorios = '\\'


# archivo = 'directorio' + separadores_directorios + 'archivo.txt'


# print(archivo)


# exit()




uname = os.uname()

sysname = uname.sysname
nodename = uname.nodename
release = uname.release
version = uname.version
machine = uname.machine

print("Sistema operativo: ", sysname)
print("Nombre del nodo: ", nodename)
print("Versión del sistema: ", release)
print("Versión: ", version)
print("Arquitectura: ", machine)


