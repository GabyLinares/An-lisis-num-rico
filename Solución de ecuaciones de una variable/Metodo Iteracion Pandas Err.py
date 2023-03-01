import numpy as np
import pandas as pd
import math

def iteracion_punto_fijo(g, x0, tol=1e-4, max_iter=20):

    x = x0
    iterations = [(0, x, np.nan)]
    for i in range(1, max_iter+1):
        x_new = g(x)
        error = (abs(x_new - x) / abs(x_new))*100
        iterations.append((i, x_new, error))
        if error < tol:
            break
        x = np.double(x_new)

    data = {'Iteración': [it[0] for it in iterations],
            'Aproximación': [it[1] for it in iterations],
            'Error porcentual': [it[2] for it in iterations]}
    df = pd.DataFrame(data)
    return iterations, df

# Poner funcion aca:
def f(x):
    return(math.e**x - 4*(x**2) - 8*x)
x0 = 1
iterations, df = iteracion_punto_fijo(f, x0)

print(df)
