# -*- coding: utf-8 -*-
"""
SOLUCION DE ECUACIONES DE UNA VARIABLE - SECANTE

NO USA PRETTY TABLES

"""
import math

# FUNCION PROBLEMA

# 1. math.e**x - 4 + x
# 2. x - 0.2*math.sin(x) - 0.5
# 3. math.e**(x/2) - x**2 - 3*x
# 4. (math.e**x)*math.cos(x) - x**2 + 3*x
# 5. 0.5*(x**3) + x**2 - 2*x - 5
# 6. math.e**x - 4*(x**2) - 8*x 

def f(x):
    return(math.e**x - 4*(x**2) - 8*x)

# FUNCION METODO SECANTE

def secante(f, x0, x1, err, its_deseadas):
    """
    Encuentra una aproximación de la raíz de la función f(x) utilizando el método de la secante.

    Parámetros:
    f (función): La función de la cual se busca una raíz.
    x0 (float): Primer punto de inicio para el método de la secante.
    x1 (float): Segundo punto de inicio para el método de la secante.
    err (float): Tolerancia para el error relativo del método.
    max_iter (int): El número máximo de iteraciones permitidas.

    Retorna:
    float: Una aproximación de la raíz de la función f(x).
    """
    print("Iteración\t x0\t\t x1\t\t x2\t\t f(x2)\t\t err")
    for i in range(its_deseadas):
        fx0 = f(x0)
        fx1 = f(x1)
        x2 = x1 - (fx1 * (x1 - x0)) / (fx1 - fx0)
        fx2 = f(x2)
        print(f"{i+1}\t\t {x0:.6f}\t {x1:.6f}\t {x2:.6f}\t {fx2:.6f}\t {abs((x2 - x1)/x2) * 100}")
        if abs((x2 - x1)/x2) * 100 < err:
            return x2
        x0, x1 = x1, x2
    raise ValueError("El método de la secante no converge.")

# IMPLEMENTACION

raiz_aproximada = secante(f, 2, 3, 0.05, 100)
print(f"\nUna aproximación de la raíz es: {raiz_aproximada}")
