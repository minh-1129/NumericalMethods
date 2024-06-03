'''
Phuong phap diem sai
'''
import numpy as np

def f(x: float) -> float:
    return x - np.cos(x)

def false_position(p0 : float, p1 : float, max_iter : int, tol: float):
    i = 1
    while i <= max_iter:
        p = p1 - (f(p1) * (p1 - p0)) / (f(p1) - f(p0))
        print(p0, p1)
        print(p)

        #dieu kien dung
        if abs(p1 - p) < tol:
            print(f"The result is {p} found at iteration {i}")
            print(f(p))
            return
        if (f(p) * f(p1) < 0):
            p0 = p1
        else:
            p1 = p
        i += 1
    print(f"False Position Method failed after {max_iter} iterations")

false_position(p0 = 0.8, p1 = 1, max_iter = 10, tol = 0.001)