import numpy as np

A = np.array([[4, 1], [1, -2]]) 
#A = A - 5 * np.array([[1, 0], [0, 1]])

x = np.array([[1, 0]]).T 
  

tol = 1e-6

max_iter = 10

lamda = 0
x_prev = x
for i in range(max_iter): 
    y = A @ x_prev
    for i in y:
        if abs(i) > maxy:
            maxy = i    
    xk = y / maxy
    x_prev = xk
    print(y)

