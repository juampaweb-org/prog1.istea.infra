

import errno

nombre_archivo = '/var/www/html/prog1.istea.infra/unidad-11/agendanoexiste.txt'

try:
    stream = open(nombre_archivo, 'rt')
    print("El archivo se abrió correctamente...")
    stream.close()

except IOError as exc:
    print(exc.errno)
    print(errno.ENOENT)
    exit()
    if exc.errno == errno.ENOENT:
        print("El archivo no existe...")
    # print(exc.errno)

# errno.EACCES → Permiso denegado


# errno.EACCES → Permiso denegado
# errno.EBADF → Número de archivo incorrecto
# errno.EEXIST → Archivo existente
# errno.EFBIG → Archivo demasiado grande
# errno.EISDIR → Es un directorio
# errno.EMFILE → Demasiados archivos abiertos
# errno.ENOENT → El archivo o directorio no existe
# errno.ENOSPC → No queda espacio en el dispositivo




# mode = 'w' -> write
# mode = 'a' -> append
# mode = 'r' -> read
# mode = 'r+' -> read and write   # acá el archivo debe existir
# mode = 'w+' -> write and read   # acá el archivo se crea si no existe
