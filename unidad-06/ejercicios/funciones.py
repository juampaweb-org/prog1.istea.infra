

def discriminante(a, b, c):
    return (b**2 - 4*a*c)

def es_raiz_positiva(a, b, c):
    print("discriminante: ", discriminante(a, b, c))
    exit()
    return discriminante(a, b, c) >= 0

def es_raiz_negativa(a, b, c):
    return discriminante(a, b, c) < 0

def es_raiz_nula(a, b, c):
    if discriminante(a, b, c) == 0:
        return True
    else:
        return False

def resolver_x1(a, b, c):
    return (-b + discriminante(a, b, c)**0.5) / (2*a)

def resolver_x2(a, b, c):
    return (-b - discriminante(a, b, c)**0.5) / (2*a)

