# -*- coding: utf-8 -*-
"""
SOLUCION DE ECUACIONES DE UNA VARIABLE - FALSA POSICION

aqui c = b - (f(b)(b-a)) / (f(b)-f(a))
"""

from prettytable import PrettyTable
import math

#tab.add_rows(table[1:])

# FUNCIÓN PARA DETECTAR SIGNOS OPUESTOS

def oppositeSigns(x, y):
    return ((x > 0 and y < 0) or (x < 0 and y > 0))

# FUNCION PROBLEMA

# 1. math.e**x - 4 + x
# 2. x - 0.2*math.sin(x) - 0.5
# 3. math.e**(x/2) - x**2 - 3*x
# 4. (math.e**x)*math.cos(x) - x**2 + 3*x
# 5. 0.5*(x**3) + x**2 - 2*x - 5
# 6. math.e**x - 4*(x**2) - 8*x 

def f(x):
    return(math.e**x - 4*(x**2) - 8*x)

# FUNCION ERR

def err(Pn_1, Pn):
    return(abs((Pn_1 - Pn)/Pn_1) * 100)

# CREACION DE TABLA

table = [['it', 'a', 'b', 'f(a)', 'f(b)', 'c', 'f(c)', 'err']]
tab = PrettyTable(table[0])

# FUNCION FALSA POSICION

def falsa_posicion(f, a, b, its_deseadas):
    """
    Encuentra una aproximación de la raíz de la función f(x) utilizando el método de la falsa posicion.
    (USA PRETTY TABLES)

    Parámetros:
    f (función): La función de la cual se busca una raíz.
    a (float), b (float): Puntos del intervalo [a,b].
    its_deseadas (int): El número máximo de iteraciones permitidas.

    Retorna:
    float: Una aproximación de la raíz de la función f(x).
    """
    
    it = 0
    for i in range(its_deseadas):
        add = []
        Pn_1 = b - ((f(b)*(b-a)) / (f(b)-f(a)))

        # evaluacion de condiciones

        if oppositeSigns(f(a), f(b - ((f(b)*(b-a)) / (f(b)-f(a))))):
            a = a
            b = b - ((f(b)*(b-a)) / (f(b)-f(a)))

        elif oppositeSigns(f(b - ((f(b)*(b-a)) / (f(b)-f(a)))), f(b)):
            a = b - ((f(b)*(b-a)) / (f(b)-f(a)))
            b = b

        elif f(b - ((f(b)*(b-a)) / (f(b)-f(a)))) == 0:
            print(b - ((f(b)*(b-a)) / (f(b)-f(a))), "F_c ES UN CERO")

        else:
            print("LA SOLUCION NO ES POSIBLE")
            break

        it += 1
        Pn = b - ((f(b)*(b-a)) / (f(b)-f(a)))
        add = [it, a, b, f(a), f(b), b - ((f(b)*(b-a)) / (f(b)-f(a))), f(b - ((f(b)*(b-a)) / (f(b)-f(a)))), err(Pn_1, Pn)]
        table.append(add)

    return add

# IMPLEMENTACION

a = 0
b = 1
it = 0
its_deseadas = 11


add = [it, a, b, f(a), f(b), b - ((f(b)*(b-a)) / (f(b)-f(a))), f(b - ((f(b)*(b-a)) / (f(b)-f(a)))), "n/a"]
table.append(add)

falsa_posicion(f, a, b,its_deseadas)
    
tab.add_rows(table[1:])
print(tab)



