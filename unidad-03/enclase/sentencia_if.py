


alumno_nombre = "Federico"
alumno_edad = 15

print( alumno_nombre + " tiene " + str(alumno_edad) + " años" )





if alumno_edad >= 18:
    print("El alumno " + alumno_nombre + " es mayor de edad")
    print("Puede ingresar al bar")
elif alumno_edad == 17:
    print("El alumno " + alumno_nombre + " es menor de edad, tiene 17 años")
    print("Puede ingresar al bar con un mayor de edad")
elif alumno_edad == 16:
    print("El alumno " + alumno_nombre + " es menor de edad, tiene 16 años")
    print("Puede ingresar al bar con un mayor de edad")
else:
    print("El alumno " + alumno_nombre + " es menor de edad")
    print("No puede ingresar al bar")

print("Fin del programa")