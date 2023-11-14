

# metodo strptime

from datetime import datetime

fecha_personalizada = "23/06/23"
print(fecha_personalizada)

fecha_personalizada_objeto = datetime.strptime( fecha_personalizada, "%d/%m/%y" )


print(fecha_personalizada_objeto.strftime("%d - %m - %y"))

