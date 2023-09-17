



Hola chicos,
en principio muy bien por haberlo finalizado y entregado a tiempo.
También en la mayoría de los casos funciona correctamente.
Así que felicitaciones, buen trabajo! Y les marco debajo una devolución de lo que se puede mejorar....


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



- Siempre conviene validar cuando el usuario va a hacer un ingreso, por ejemplo si ingresamos una letra en vez de un número nos arroja un error.
```python
equipo-2/ejercicio_1 $ python ejercicio.py 
Ingrese A
d
Traceback (most recent call last):
  File "/var/www/html/prog1.istea.infra/unidad-06/ejercicios/equipo-2/ejercicio_1/ejercicio.py", line 7, in <module>
    a = int(input())
ValueError: invalid literal for int() with base 10: 'd'
```

