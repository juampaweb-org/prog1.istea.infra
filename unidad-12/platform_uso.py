


import platform

sistema_operativo = platform.system()
print("Sistema operativo: ", sistema_operativo)
print("-------------------------------------------------")

version_sistema = platform.version()
print("Versión del sistema: ", version_sistema)
print("-------------------------------------------------")

arquitectura = platform.architecture()
print("Arquitectura: ", arquitectura)
print("-------------------------------------------------")


interprete = platform.python_implementation()
print("Interprete: ", interprete)
print("-------------------------------------------------")

version = platform.python_version()
version_en_tupla = platform.python_version_tuple()
print("-------------------------------------------------")

print("Versión: ", version)
print("Versión en tupla: ", version_en_tupla)
print("-------------------------------------------------")

