

# metodo strftime

from datetime import date, time, datetime

fecha_personal = date(2001, 6, 23)
print(fecha_personal.strftime("%d/%m/%y"))

fecha_hora_personal = datetime(2001, 6, 23, 14, 30, 59, 100)
print(fecha_hora_personal.strftime( "anio %Y-%B-%d || %H:%M:%S" ))

