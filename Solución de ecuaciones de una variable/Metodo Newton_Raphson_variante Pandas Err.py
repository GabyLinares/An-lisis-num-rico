import numpy as np
import pandas as pd

def newton_raphson_von_mises(f, df, d2f, x0, tol=1e-6, max_iter=100):

    x = x0
    iterations = [(0, x, np.nan)]
    for i in range(1, max_iter+1):
        x_new = x - (f(x) - np.sin(np.pi/6))/(df(x) - (np.pi/6)*d2f(x))
        error = abs(x_new - x) / abs(x_new)
        iterations.append((i, x_new, error))
        if error < tol:
            break
        x = x_new

    data = {'Iteración': [it[0] for it in iterations],
            'Aproximación': [it[1] for it in iterations],
            'Error porcentual': [it[2] for it in iterations]}
    df = pd.DataFrame(data)
    return iterations, df

# Poner funcion aca 
def f(x):
    return x - 0.2*np.sin(x) - 0.5
def df(x):
    return -0.2*np.cos(x) 
def d2f(x):
    return 0.2*np.sin(x) 
x0 = 1
iterations, df = newton_raphson_von_mises(f, df, d2f, x0)

print(df)
