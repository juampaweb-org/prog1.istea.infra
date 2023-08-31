


# ejercicio 9
# Hacer un programa que permita saber si un año es bisiesto.
# Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.



# anio = int(input("Ingrese un año: "))




# if anio % 4 == 0 and anio % 100 != 0:
#     if anio % 400 != 0:
#         print("El año NO es bisiesto")
#     else:
#         print("El año es bisiesto")
# else:
#     print("El año NO es bisiesto")

anio = int(input("Ingrese un año: "))

if anio % 4 == 0:
    if anio % 100 == 0: # si es divisible x 100
        if anio % 400 == 0:
            print ("el año", anio ,  "un año bisiesto.")
        else:
            print ("El año" , anio , "no es bisiesto")
    else:
        print ("El año", anio , "es bisiesto")
else:
    print ("El año" , anio , "no es bisiesto")

