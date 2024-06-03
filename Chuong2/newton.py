import numpy as np

def f(x: float) -> float:
    return x - np.cos(x)

def df(x: float) -> float:
    return 1 + np.sin(x)

history = list()
def newton(p0 : float, max_iter : int, tol: float):
    i = 0
    history.clear()
    while i < max_iter:
        p = p0 - f(p0) / df(p0)
        
        history.append(p)
        
        #dieu kien dung
        if abs(p - p0) < tol:
            print(f"The result is {p} fount at iteration {i}")
            return 
        
        p0 = p
        i = i + 1
    print(f"Newton Method failed after {max_iter} iterations")

newton(p0 = 0, max_iter = 100, tol = 1e-6)
print(history)