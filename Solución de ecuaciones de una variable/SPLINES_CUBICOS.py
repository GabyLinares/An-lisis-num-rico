import numpy as np
import matplotlib.pyplot as plt

x = np.array([2006,2008,2011,2012,2015,2017,2018,2020,2021,2022])
y = np.array([0.6543, 0.6737, 0.6679, 0.6909, 0.686, 0.684, 0.681, 0.691, 0.695, 0.696])
plt.plot(x,y,'bo')
plt.legend()
plt.show()

n = len(x)
h = np.diff(x)
A = np.zeros((n, n))
A[0, 0] = 1
A[n-1, n-1] = 1
for i in range(1, n-1):
    A[i, i-1] = h[i-1]
    A[i, i] = 2*(h[i-1]+h[i])
    A[i, i+1] = h[i]
b = np.zeros(n)
for i in range(1, n-1):
    b[i] = 3/h[i]*(y[i+1]-y[i]) - 3/h[i-1]*(y[i]-y[i-1])
c = np.linalg.solve(A, b)
a = y[:-1]
b = (y[1:]-y[:-1])/h - h/3*(2*c[:-1]+c[1:])
d = (c[1:]-c[:-1])/(3*h)

coeficientes = []
print("   i      ai      bi      ci      di")
for i in range(n-1):
    print(f"   {i}   {a[i]:.8f}   {b[i]:.8f}   {c[i]:.8f}   {d[i]:.8f}")
    coeficientes.append([a[i], b[i], c[i], d[i]])

xx = np.linspace(x[0], x[-1], 100)
yy = np.zeros_like(xx)
for i in range(n-1):
    idx = (xx >= x[i]) & (xx <= x[i+1])
    xx_sub = xx[idx] - x[i]
    yy[idx] = a[i] + b[i]*xx_sub + c[i]*xx_sub**2 + d[i]*xx_sub**3

plt.plot(xx, yy, label="spline cúbico")
plt.plot(x, y, 'o', label="datos")
plt.legend()
plt.show()

# Encontrar valores de años que faltan en MATLAB
print(coeficientes)
