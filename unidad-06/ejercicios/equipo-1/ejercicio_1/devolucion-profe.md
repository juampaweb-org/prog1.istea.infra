

Hola chicos,
en principio muy bien por haberlo finalizado y entregado a tiempo.
También en la mayoría de los casos funciona correctamente.
Asíq ue felicitaciones, buen trabajo! Y les marco debajo una devolución de lo que se puede mejorar....


Les hago una devolución del script realizado, que no es tomado con puntaje, pero si como notas conceptuales.


- Detecté un caso en donde el script no funciona correctamente, lo expongo debajo a ver si lo pueden salvar:
```python
ingrese valores a, b y c dela ecuacion cuadratica
ingrse valor de A: 0
ingrse valor de B: 2
ingrse valor de C: -2
Traceback (most recent call last):
  File "/var/www/html/prog1.istea.infra/unidad-06/ejercicios/equipo-1/trabajo_clase_ejercicio1.py", line 27, in <module>
    resultado1 = ((int(varB)* -1) + sqrt(resdiscriminante)) / (2 * int(varA))
ZeroDivisionError: float division by zero
```


- Las funciones principales las tenemos que separar del script principal para poner un orden.
Entonces:
    - Las funciones las dejamos en un archivo aparte, por ejemplo: funciones_cuadratica.py
    - El script principal lo dejamos en un archivo aparte, por ejemplo: main.py
    - En el script principal importamos las funciones del archivo funciones_cuadratica.py
    - En el script principal llamamos a las funciones importadas para que se ejecuten.

- Nombres de las variables deben ser más descriptivas, y utilizar guion bajo para separar palabras, por ejemplo:
    - varA -> coeficiente_a
    - varB -> coeficiente_b
    - varC -> coeficiente_c
    - resdiscriminante -> result_discriminante
    - resultado1 -> result_1
    - resultado2 -> result_2

- Por ultimo, siempre conviene validar cuando el usuario va a hacer un ingreso, por ejemplo si ingresamos una letra en vez de un número nos arroja un error.
```python
ingrse valor de A: d
ingrse valor de B: 2
ingrse valor de C: 3
Traceback (most recent call last):
  File "/var/www/html/prog1.istea.infra/unidad-06/ejercicios/equipo-1/trabajo_clase_ejercicio1.py", line 19, in <module>
    resdiscriminante = discriminante(varA,varB,varC)
  File "/var/www/html/prog1.istea.infra/unidad-06/ejercicios/equipo-1/trabajo_clase_ejercicio1.py", line 2, in discriminante
    ecuacion = int(varB) ** 2 - (4 * int(varA) * int(varC))
ValueError: invalid literal for int() with base 10: 'd'
```

