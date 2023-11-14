

import os

print("Path actual: ", os.getcwd())
print("Vemos lo que hay acá: ", os.listdir('.'))


os.makedirs("/var/www/html/prog1.istea.infra/unidad-12/dir_uno/dir_dos/dir_tres/")
os.mkdir("/var/www/html/prog1.istea.infra/unidad-12/otro-directorio/")

# Vamos a movernos de directorio
os.chdir("/var/www/html/prog1.istea.infra/unidad-12/dir_uno/dir_dos/dir_tres/")
print("Path actual dentro de dir3 (supuestamente): ", os.getcwd())

os.makedirs("dir_cuatro/dir_cinco/dir_seis/")

