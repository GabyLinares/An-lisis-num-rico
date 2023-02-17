# -*- coding: utf-8 -*-
"""
SOLUCION DE ECUACIONES DE UNA VARIABLE - BISECCION

aqui c = (a + b)/2
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


add = [it, a, b, f(a), f(b), (a + b)/2, f((a + b)/2), "n/a"]
table.append(add)

for i in range(its_deseadas):
    add = []
    Pn_1 = (a + b)/2

    # evaluacion de condiciones

    if oppositeSigns(f(a), f((a + b)/2)):
        a = a
        b = (a + b)/2

    elif oppositeSigns(f((a + b)/2), f(b)):
        a = (a + b)/2
        b = b

    elif f((a + b)/2) == 0:
        print((a + b)/2, "F_c ES UN CERO")

    else:
        print("LA SOLUCION NO ES POSIBLE")
        break

    it += 1
    Pn = (a + b)/2
    add = [it, a, b, f(a), f(b), (a + b)/2, f((a + b)/2), err(Pn_1, Pn)]
    table.append(add)
    

tab.add_rows(table[1:])
print(tab)



