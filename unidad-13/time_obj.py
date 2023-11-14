

# time(hour, minute, second, microsecond, tzinfo, fold)

from datetime import time

hora_personalizada = time(14, 30, 59, 100000)

print("Hora personalizada: ", hora_personalizada)
print("Hora: ", hora_personalizada.hour)
print("Minuto: ", hora_personalizada.minute)
print("Segundo: ", hora_personalizada.second)
print("Microsegundo: ", hora_personalizada.microsecond)


