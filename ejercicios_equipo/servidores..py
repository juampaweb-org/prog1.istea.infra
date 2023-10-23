

"""
Vamos a armar un diccionario de 100 servidores, en donde la clave va a ser el numero de servidor que va del 1 al 100,
y los valores por cada servidor, va a ser una lista, con (distro, ram, disco, ip, estado)
Los valores de distro son random entre: ubuntu, debian, centos, fedora, suse
Los valores de ram son random entre: 64, 128, 256 (en GB, pero ponemos el numero)
Los valores de disco son random entre: 1.92, 3.84, 7.68 (en TB, pero ponemos el numero)
Los valores de IP son 123.543.23.xxx (el xxx va desde 0 hasta 255)
Los valores de estado son: online, offline, warning, critical


La idea es en principio generar el diccionario, mostrarlo en pantalla,
y realizar diferentes funciones en donde pueda modificar los diferentes datos.
ejemplo -> modificar_distro(3, 'debian')   Le digo que el servidor 3, ahora tiene distro debian

Y otra función que me muestre el servidor que le pido:
mostrar_servidor(3)  -> me muestra el servidor 3, con todos sus datos


"""



servidores = {
    1: ['ubuntu', 64, 1.92, '123.543.23.1', 'online'],
    2: ['debian', 128, 3.84, '123.543.23.2', 'offline'],
}