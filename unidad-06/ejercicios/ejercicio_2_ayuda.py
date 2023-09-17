"""
2do Ejercicio-
– Parte A
Pedir una palabra al usuario.
Avisar si dicha palabra es palíndromo, es decir capicua.
Por ejemplo la palabra: amor -> Roma
No debe importar mayúscula/minúsculas
– Parte B
Ahora pedir una frase, y determinar si es palindromo o no

Ejemplo de frases palindromas:
https://www.esquire.com/es/actualidad/libros/a40309148/palindromos-ejemplos-palabras-fra
ses/


"""



"""
AYUDA
Debemos recorrer el string ingresado e ir llenando una lista con cada caracter.
Luego debemos utilizar los métodos de listas para invertir. método sort()
Y comparar si la lista invertida es igual a la lista original.

Ejemplo:
palabra = "amor"
lista_palabra = []
for i in palabra:
    lista_palabra.append(i)

Luego ordenamos la lista, y vamos a comparar si la lista invertida es igual a la lista original.

"""
