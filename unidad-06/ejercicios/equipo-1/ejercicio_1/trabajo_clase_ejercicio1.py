def discriminante ( varA, varB , varC ):
    ecuacion = int(varB) ** 2 - (4 * int(varA) * int(varC))
    if ecuacion < 0:
        return "error"
    elif ecuacion == 0:
        return 0
    else:
        return ecuacion
    
from math import sqrt 

print("ingrese valores a, b y c dela ecuacion cuadratica")
varA = input("ingrse valor de A: ")
varB = input("ingrse valor de B: ")
varC = input("ingrse valor de C: ")

#print(discriminante(varA,varB,varC))

resdiscriminante = discriminante(varA,varB,varC)

if resdiscriminante == "error":
    print("no tiene solucion")
elif resdiscriminante == 0:
    resultado = (int(varB)* -1)/ (2 * int(varA))
    print(resultado)
else:
    resultado1 = ((int(varB)* -1) + sqrt(resdiscriminante)) / (2 * int(varA))
    resultado2 = ((int(varB)* -1) - sqrt(resdiscriminante)) / (2 * int(varA))

    print("los resultados son: ", resultado1 , resultado2)


