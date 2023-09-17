import funciones

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if funciones.es_raiz_positiva(a, b, c):
    # como tiene positiva va a tener dos soluciones
    print("La ecuación tiene dos soluciones")
    x_1 = funciones.resolver_x1(a, b, c)
    x_2 = funciones.resolver_x2(a, b, c)
    resultado = "x_1: " + str(x_1) + " x_2: " + str(x_2)

elif funciones.es_raiz_nula(a, b, c):
    print("La ecuación tiene una solución doble")
    x_1 = funciones.resolver_x1(a, b, c)
    resultado = "x_1: " + str(x_1) + " doble solución"

elif funciones.es_raiz_negativa(a, b, c):
    print("La ecuación no tiene solución")
    resultado = "No tiene solución"

else:
    print("La ecuación no tiene solución, entró en el else")
    resultado = "No tiene solución, entró en el else"

print("RESULTADO: ")
print(resultado)

