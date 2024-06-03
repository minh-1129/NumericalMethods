import numpy as np

#A = np.array([[4, 1], [1, -2]]) 
A = np.array([[0, 1], [2, -2]]) 
#A = A - 5 * np.array([[1, 0], [0, 1]])

x = np.array([[1, 0]]).T 
  

tol = 1e-6

max_iter = 10

lamda = 0
x_prev = x
for i in range(max_iter): 
    y = np. linalg. inv(A) @ x_prev
    maxy = -np.inf
    for i in y:
        if abs(i) > maxy:
            maxy = i
    xk = y / maxy
    x_prev = xk
    
    #Rayleigh Quotient
    lamda = (xk.T @ np.linalg.inv(A) @ xk) / (xk.T @ xk) 
    print(f"Iteration {i}: ")
    print(f"y: {y}")
    print(f"x: {xk}")
    print(f"lam:{1/lamda + 3}")

print(1/lamda)