"""
Vamos a pedirle al usuario que vaya ingresando diferentes palabras, y las vamos a ir guardando en una lista.
Cuando el usuario ingrese una palabra vacia, dejamos de pedirle palabras. Es decir aprente enter sin ingresar nada.
Luego las vamos a mostrar de manera ordenadas alfabetica, pasadas a minusculas.
Y luego vamos a mostrar la cantidad de palabras que se ingresaron.
Y luego vamos a mostrar la cantidad de letras que hay en total.

ejemplo:
perro, casa, gato, auto, arbol

ordenadas alfabeticamente:
arbol, auto, casa, gato, perro

cantidad de palabras: 5
cantidad de letras: 22


"""
palabras = [] #creamos una lista vacia para almacenar las palabras

while True:
    palabra = input("Ingrese una palabra (o deje en blanco para continuar): ")
    if palabra == "":
        break
    palabras.append(palabra.lower()) #suma las palabras

palabras.sort() #ordena las palabras alfabeticamente y modifica el objeto

sorted(palabras) #ordena las palabras alfabeticamente, pero no modifica el objeto



print("Palabras ordenadas alfabéticamente:") 
for palabra in palabras:
    print(palabra)
   

cantidad_palabras = len(palabras) #calcula la cantidad de palabras
cantidad_letras = sum(len(palabra) for palabra in palabras) #suma la cantidad de letras     
print ("La cantidad de palabras es:", cantidad_palabras) 
print ("La cantidad de letras es:", cantidad_letras) 
exit()

