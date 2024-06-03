'''
Diem bat dong
'''
import numpy as np

def g(x : float) -> float:
    return np.cos(x)

def fixed_point(p0, max_iter : int, tol : float) -> float:
    i = 1
    while i <= max_iter:
        p = g(p0)
        print(p0, p)
        
        #dieu kien dung
        if abs(p - p0) < tol:
            print(f"The result is {p} fount at iteration {i}")
            return p
        
        p0 = p
        
        i = i + 1
    
    print(f"Fixed Point Method failed after {max_iter} iterations")
    return np.inf

fixed_point(1, 100, 1e-6)