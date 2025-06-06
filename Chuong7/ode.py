import numpy as np

def f(x: float, y: float):
    return 1 + x ** 2 + y

def df(x: float, y: float):
    return 2 * x + f(x, y)

def taylor_method(x0: float, y0: float, h: float, max_iter: int):
    #order 2
    #y_(i + 1) = y_i + h * f + (h ** 2 / 2) * df
    x, y = [], []
    x.append(x0)
    y.append(y0)
    for i in range(max_iter):
        y0 = y0 + h * f(x0, y0) + (h ** 2 / 2) * df(x0, y0)
        x0 += h
        x.append(x0)
        y.append(y0)
    return x, y

def midpoint_method(x0: float, y0:float, h: float, max_iter: int):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    for i in range(max_iter):
        y_mid = y + h / 2 * f(x0, y0)
        x_mid = x + h / 2
        y = y + h * f(x_mid, y_mid)
        x = x_mid + h / 2
        xl.append(x)
        yl.append(y)
    return xl, yl   

def heun_method(x0: float, y0: float, h: float, max_iter: int):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    for i in range(max_iter):
        y_pred = y + h * f(x, y)
        y = y + (h / 2) * (f(x, y) + f(x + h, y_pred))
        x += h
        xl.append(x)
        yl.append(y)
    return xl, yl

def runge_kutta_method(x0: float, y0: float, h: float, max_iter: int):
    xl, yl = [], []
    x, y = x0, y0
    xl.append(x)
    yl.append(y)
    for i in range(max_iter):
        k1 = f(x, y)
        k2 = f(x + 0.5 * h, y + 0.5 * k1 * h)
        k3 = f(x + 0.5 * h, y + 0.5 * k2 * h)
        k4 = f(x + h, y + k3 * h)
        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xl.append(x)
        yl.append(y)

    return xl, yl

print("Euler method:")
for i in range(2):
    print(taylor_method(0, 1, 0.1, 5)[i])
print("--------------------")
print("Midpoint method:")
for i in range(2):
    print(midpoint_method(0, 1, 0.1, 5)[i])
print("--------------------")
print("Heun method:")
for i in range(2):
    print(heun_method(0, 1, 0.1, 5)[i])
print("--------------------")
print("Runge-Kutta method:")
for i in range(2):
    print(runge_kutta_method(0, 0.5, 0.2, 5)[i])
print("--------------------")