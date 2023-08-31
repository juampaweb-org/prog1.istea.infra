











# metodo lstrip() y rstrip()
# Remover espacios a la derecha o a la izquierda


cadena = "Python es un lenguaje multiproposito               "

cadena_espacios_izq = "               Python es un lenguaje multiproposito "


remuevo_espacios = cadena.rstrip()


remuevo_espacios_izq = cadena_espacios_izq.lstrip()

otra_cadena = "empieza otra cadena"

print(remuevo_espacios_izq + otra_cadena)
