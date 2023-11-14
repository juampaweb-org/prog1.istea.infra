

# modulo subprocess


import subprocess


comando = "ls -l"

resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Imprimimos el resultado

print(type(resultado))

print("Codigo de salida: ", resultado.returncode)
print("Salida estandar: ", resultado.stdout.decode())
print("Error estandard: ", resultado.stderr.decode())


