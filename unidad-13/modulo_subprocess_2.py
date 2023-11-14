

import subprocess

# Definimos el comando a ejecutar
comando = "ls"

# Ejecutamos el comando utilizando subprocess.run
# - shell=True permite ejecutar comandos de la shell
# - stdout=subprocess.PIPE captura la salida estándar del comando
# - stderr=subprocess.PIPE captura la salida de error del comando
resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Imprimimos la salida estándar del comando
print("Salida estándar:")
print(resultado.stdout.decode("utf-8"))

# Imprimimos la salida de error del comando en caso de haberla
print("Salida de error:")
print(resultado.stderr.decode("utf-8"))



