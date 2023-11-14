

from datetime import datetime

fecha_hora = datetime(2019, 10, 15, 14, 30, 45, 1000, None)

print(" Fecha y hora: ", fecha_hora)
print(" Año: ", fecha_hora.year)
print(" Mes: ", fecha_hora.month)
print(" Día: ", fecha_hora.day)
print("--------------------------------")

print("Hora: ", fecha_hora.time())
print("Hora especifica: ", fecha_hora.time().hour)
print("Minuto: ", fecha_hora.time().minute)
print("Segundo: ", fecha_hora.time().second)
print("Microsegundo: ", fecha_hora.time().microsecond)


print("Fecha y hora actual: ", datetime.today())

# strftime







