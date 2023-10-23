

"""
Vamos a armar dos diccionarios.

Uno va a tener de clave desde el 1 al 100 que son los servidores, y de valor un hash que va a ser formado por random de 20 caracteres.

Y el otro va a ir recorriendo este diccionario, y la clave va a ser el hash, y luego el valor una lista con lo siguiente:
Los valores de distro son random entre: ubuntu, debian, centos, fedora, suse
Los valores de IP son 123.543.23.xxx (el xxx va desde 0 hasta 255)
Los valores de estado son: online, offline, warning, critical


La idea es en principio generar el diccionario, mostrarlo en pantalla, (el del hash con los datos del servidor)
y realizar diferentes funciones en donde pueda modificar los diferentes datos.
ejemplo -> modificar_distro(3, 'debian')   Le digo que el servidor 3, ahora tiene distro debian

Y otra función que me muestre el servidor que le pido:
mostrar_servidor(3)  -> me muestra el servidor 3, con todos sus datos




"""





servidores_hash = {
    1: 'hjdhjwkjjshss',
    2: 'hjdhjwkjjshsskj2',
}

servidores = {
    'hjdhjwkjjshss': ['123.543.23.4', 'debian', 'online'],
    'hjdhjwkjjshsskj2': ['123.543.23.5', 'ubuntu', 'offline'],
}