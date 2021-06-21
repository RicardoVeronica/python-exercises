"""
File: algebra.py
Author: Ricardo Veronica Duran
Email: setcain00@gmail.com
Github: https://github.com/setcain
Description: De lenguaje algebraico a expresiones matematicas
"""


# La suma de dos numeros
# suma = lambda x, y: x + y
def suma(x, y):
    return x + y


# La extraccion de dos numeros
# resta = lambda x, y: x - y
def extraccion(x, y):
    return x - y


# El producto de dos numeros
multiplicacion = lambda x, y: x * y

# La razon o el cociente de dos numeros
division = lambda x, y: x / y

# El doble de un numero
doble = lambda x: x * 2

# El triple de un numero
triple = lambda x: x * 3

# El cuadrado de un numero
cuadrado = lambda x: x ** 2

# El cubo de un numero
cubo = lambda x: x ** 3

# La mitad de un numero
mitad = lambda x: x / 2

# La tercera parte parte de un numero
tercera_parte_numero = lambda x: x / 3

# El doble de la suma de dos numeros
doble_suma_dos_numeros = lambda x, y: 2 * (x + y)

# El triple de la diferencia de dos numeros
triple_diferencia_dos_numeros = lambda x, y: 3 * (x - y)

# La suma de dos numeros
suma_dos_numeros = lambda x, y: x + y

# Un numero aumentado en tres
numero_aumentado_tres = lambda x: x + 3

# Un numero disminuido en cinco
numero_disminuido_cinco = lambda x: x - 5

# La diferencia entre un numero y 8
diferencia_numero_y_ocho = lambda x: x - 8

# El doble del producto de dos numeros
doble_producto_dos_numeros = lambda x, y: 2 * (x * y)

# El triple del cociente de dos numeros
triple_cociente_dos_numeros = lambda x, y: 3 * (x / y)

# El cuadrado de la diferencia de dos numeros
cuadrardo_diferencia_dos_numeros = lambda x, y: (x - y) ** 2

# La suma del cuadrado de dos numeros
suma_cuadrado_dos_numeros = lambda x, y: x**2 + y**2

# El sucesor de un numero
sucesor_nuemero = lambda x: x + 1

# El antecesor de un numero
antecesor_numero = lambda x: x - 1

# Dos numeros consecutivos
dos_numeros_consecutivos = lambda x: f"{x}, {x + 1}"

# Tres numeros consecutivos
tres_numeros_consecutivos = lambda x: f"{x}, {x + 1}, {x + 2}"

# Un numero par
numero_par = lambda x: x * 2

# La suma de tres numeros pares
suma_tres_numeros_pares = lambda x, y, z: (x * 2) + (y * 2) + (z * 2)

# Numero impar
numero_impar = lambda x: (x * 2) - 1

# Numero de tres cifras
def numero_tres_cifras(x, y, z):
    if (x < 10 and y < 10 and z < 10): return (x * 100)+ (y * 10) + z
    else: print('Cada argumento tiene que ser de una cifra')

# El cubo de la quinta parte de un numero
cubo_quita_parte_numero = lambda x: (x // 5) ** 3

# La quinta parte del cubo de un numero
quinta_parte_cubo_numero = lambda x: (x ** 3) // 5

# La suma de dos numeros dividida por su diferencia
suma_dos_numeros_dividida_diferencia = lambda x, y: (x + y) // (x - y)

# Las tres quintas partes de un numero aumentado en cuatro
tres_quintas_partes_numero_aumentado_cuatro = lambda x: (3 // 5) * (x + 4)

# Las tres quintas partes de un numero, aumentado en cuatro
capciosa = lambda x: ((3 // 5 ) * x) + 4

# La suma de un numero par y el triple del siguiente
suma_numero_par_triple_siguiente = lambda x: (x * 2) + (x + 1 * 3)
