

from datetime import date


def imprimir_nombre_dia_semana(dia_semana):
    if dia_semana == 0:
        print("Lunes")
    elif dia_semana == 1:
        print("Martes")
    elif dia_semana == 2:
        print("Miércoles")
    elif dia_semana == 3:
        print("Jueves")
    elif dia_semana == 4:
        print("Viernes")
    elif dia_semana == 5:
        print("Sábado")
    elif dia_semana == 6:
        print("Domingo")
    else:
        print("Error: día de la semana no válido")

    return

# metodo fromisoformat
fecha = date.fromisoformat("1986-10-20")
print(fecha)

# metodo replace
fecha = fecha.replace(year=1979, month=12, day=23)
print(fecha)
print("---------------------------------------")

# metodo weekday
mi_fecha = date.today()

dia_semana = mi_fecha.weekday()
print("Día de la semana: ", dia_semana)

imprimir_nombre_dia_semana(dia_semana)




