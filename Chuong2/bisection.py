'''
Phuong phap chia doi
'''
import numpy as np
from numpy import log2

def f(x: float) -> float:
    return x**3 - x

def bisectionMethod(f, a: float, b: float, TOL: float) -> float:
    max_iter = int(log2((b - a)/TOL))
    i = 1
    FA = f(a)

    #dieu kien dung
    while i <= max_iter:
        p = a + (b - a)/2
        print(a, b, p)
        FP = f(p)
        
        if FP == 0 or (b - a)/2 < TOL:
            print(f"The result is {p} found at iteration {i}")
            return
       
        i = i + 1
        
        if FA * FP > 0:
            a = p
            FA = FP
        else: 
            b = p
    
    print(f"Bisection Method failed after {max_iter} iterations")
        
bisectionMethod(f, a = 0.1, b = 2.3, tol = 1e-6)