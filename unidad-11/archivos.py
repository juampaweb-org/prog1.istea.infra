



nombre_archivo = '/var/www/html/prog1.istea.infra/unidad-11/agendeoeoappee.txt'

try:
    
    stream = open(nombre_archivo, 'rt')
    print("El archivo se abrió correctamente...")

    stream.close()

except Exception as error:
    print("Error al abrir el archivo...", error)







# mode = 'w' -> write
# mode = 'a' -> append
# mode = 'r' -> read
# mode = 'r+' -> read and write   # acá el archivo debe existir
# mode = 'w+' -> write and read   # acá el archivo se crea si no existe
