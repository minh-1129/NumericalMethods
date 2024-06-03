import numpy as np
import matplotlib.pyplot as plt

def least_squares_approximation(x: list, y: list, degree):
    m = len(x)
    X = np.zeros((degree + 1, degree + 1))
    for i in range(degree + 1):
        for j in range(degree + 1):
            for id in range(m):
                X[i][j] += x[id] ** (i + j)
    
    Y = np.zeros(degree + 1)
    for i in range(degree + 1):
        for id in range(m):
            Y[i] += y[id] * (x[id] ** i)
    
    a = np.linalg.solve(X, Y)
    y_fit = np.zeros(m)
    for i in range(m):
        for deg in range(degree + 1):
            y_fit[i] += a[deg] * (x[i] ** deg)
    return a, y_fit

x = [0.25 * i for i in range(5)]
y = [1, 2.5, -1.3, 4.2, 6]
a, y_fit = least_squares_approximation(x, y, 2)
print("coefficients:")
print(a)
print(y_fit - y)
x_fit = x.copy()

plt.scatter(x, y, label='data')
plt.plot(x_fit, y_fit, color='blue', label='fitted polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()