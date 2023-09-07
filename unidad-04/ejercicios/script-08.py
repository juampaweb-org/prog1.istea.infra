

"""
Escriba un programa que pida una fecha y diga si ese día existe.

El programa no tiene por qué comprobar que se escribe una fecha posterior al 15 de octubre de 1582, que fue cuando se instauró el calendario gregoriano.

Se recuerda que enero, marzo, mayo, julio, agosto, octubre y diciembre tienen 31 días, que abril, junio, septiembre y noviembre tienen 30 días y febrero tiene 28 días salvo los años bisiestos en que tiene 29.

"""


# una funcion que nos diga si el año es bisieto o no
# otra funcion que nos diga si el mes tiene 30 o 31 dias
# Hay que crear otra funcion que abarque desde la fecha indicada, que nos dé True si es posterior a 15/10/1582  False si es anterior
# Vamos a definir que el usuario ingrese la fecha en formato dd/mm/aaaa

def es_bisiesto( anio ):
    if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
        return True
    else:
        return False

def cantidad_dias( mes )
    # 01 / 02 / 03 / 04
    if mes == '01' or mes == '03' or mes == '05' or mes == '07' or mes == '08' or mes == '10' or mes == '12'
        return 31
    # Nos falta el elif para determinar los otros meses
    # Otro elif para abarcar febrero, acá podemos utilizar la función que nos determina si es bisiesto
    # y entonces retornamos la cantidad de días que tiene dicho mes que seteo el usuario.

def fecha_valida( fecha )
    # separar anio / mes / dia  -> controlar que sea valida y que ese día exista
    # 22/12/2020
    # anio = fecha_ingresada[6:10]
    # mes = fecha_ingresada[3:5]
    # dia = fecha_ingresada[0:2]
    # primero debe controlar ejemplo que el año sea mayor a 1582.
    # Y luego en función de mes y día controlar que esté bien seteado éso. (acá debemos usar las dos funciones cantidad_dias y es_bisiesto)
    # Si es correcto nos retorna True y si no False



print("Ingrese una fecha con el siguiente formato (dd/mm/aaaa)")
fecha_ingresada = input("")

if fecha_valida(fecha_ingresada) == True:
    print("Perfecto, ese día existe")
else:
    print("La fecha no es valida o no corresponde a partir de 15/10/1582")


