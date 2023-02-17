# -*- coding: utf-8 -*-
"""
SOLUCION DE ECUACIONES DE UNA VARIABLE - FALSA POSICION

aqui c = b - (f(b)(b-a)) / (f(b)-f(a))
"""

from prettytable import PrettyTable

#tab.add_rows(table[1:])

# FUNCIÓN PARA DETECTAR SIGNOS OPUESTOS

def oppositeSigns(x, y):
    return ((x > 0 and y < 0) or (x < 0 and y > 0))

# FUNCION PROBLEMA

def f(x):
    return((x ** 3) + 4 * (x ** 2) - 10)

# FUNCION ERR

def err(Pn_1, Pn):
    return(abs((Pn_1 - Pn)/Pn_1) * 100)

# CREACION DE TABLA

table = [['it', 'a', 'b', 'f(a)', 'f(b)', 'c', 'f(c)', 'err']]
tab = PrettyTable(table[0])

# IMPLEMENTACION

a = 1
b = 2

it = 0
its_deseadas = 5


add = [it, a, b, f(a), f(b), b - ((f(b)*(b-a)) / (f(b)-f(a))), f(b - ((f(b)*(b-a)) / (f(b)-f(a)))), "n/a"]
table.append(add)

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
    

tab.add_rows(table[1:])
print(tab)



