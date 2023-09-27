"""

Pedirle al usuario que escriba una frase completa.
Luego preguntarle que letra de esa frase desea contar cuantas veces aparece.
Y luego imprimir en pantalla indicando la cantidad que aparece.
Preguntar si quiere hacerlo nuevamente y volver a comenzar o terminar la ejecución.

"""



def cantidad_letras(frase, letra):
    """Devuelvo las veces que aparece un caracter en una frase"""
    cant_letras = 0
    for i in range(len(frase)):
        if frase[i] == letra:
            cant_letras += 1
    return cant_letras

continuar_script = True

while continuar_script:
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra para contar cuantas veces aparece en la frase: ")

    cant_letras = cantidad_letras(frase, letra)
    
    if cant_letras == 0:
        print("La letra", letra, "no aparece en la frase.")
    else:
        print("La letra", letra, "aparece", cant_letras, "veces en la frase.")

    sigue_ejecutando = input("Desea continuar? (s/n): ")
    if sigue_ejecutando.lower() == "n":
        continuar_script = False
        print("Fin de la ejecución.")
        exit(0)
    elif sigue_ejecutando.lower() == "s":
        continuar_script = True
    else:
        print("Opción incorrecta. Fin de la ejecución.")
        exit(1)

