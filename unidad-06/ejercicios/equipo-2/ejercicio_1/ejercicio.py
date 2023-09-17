import funcion_quad

# Paso 1
# input a,b,c

print("Ingrese A")
a = int(input())

print("Ingrese B")
b = int(input())

print("Ingrese C")
c = int(input())

# Paso 2
# Llamamos a la funcion que esta en otro archivo denominado 'funcion_quad'
    
print(funcion_quad.calcular_raices(a,b,c))

