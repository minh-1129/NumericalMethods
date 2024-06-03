'''
Phuong phap day cung
'''
import numpy as np

def f(x: float) -> float:
    return x - np.cos(x)

def secant(p0 : float, p1 : float, max_iter : int, tol: float):
    i = 1
    while i <= max_iter:
        p = p1 - (f(p1) * (p1 - p0)) / (f(p1) - f(p0))
        if (abs(p1 - p) < tol):
            print(f"The result is {p} found at iteration {i} and fp = {f(p)}")
            return
        p0 = p1
        p1 = p
        i = i + 1
    print(f"Secant Method failed after {max_iter} iterations")

secant(0, 0.5, 10, 0.0001)