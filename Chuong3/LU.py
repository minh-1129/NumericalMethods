import pprint
import numpy as np
from numpy import matmul
from numpy.linalg import inv
import scipy
import scipy.linalg


def LU_factorization(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    _, L, U = scipy.linalg.lu(A)

    print("A:")
    pprint.pprint(A)

    print("L:")
    pprint.pprint(L)

    print("U:")
    pprint.pprint(U)

    y = matmul(inv(L), b)
    print(inv(L))
    pprint.pprint(y)

    x = matmul(inv(U), y)
    pprint.pprint(x)

    return x.flatten()

def LU_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    #_, L, U = scipy.linalg.lu(A)
    if (A[0][0] == 0):
        print('Factorization impossible')
        return None, None
    
    U[0][0] = 1.0 * A[0][0] / L[0][0]
    
    for j in range(1, n):
        U[0][j] = 1.0 * A[0][j]         
        L[j][0] = 1.0 * A[j][0]/U[0][0] 
    
    for i in range (1, n-1):
        sum = 0.
        for k in range(0, i):
            sum = sum + 1.0 * L[i][k]*U[k][i]
        U[i][i] = (A[i][i] - sum) / L[i][i]
        if U[i][i] == 0:
            print('Factorization impossible')
            return None, None
        
    
        for j in range(i + 1, n):
            sumu = 0.
            for k in range(0, i):
                sumu += L[i][k] * U[k][j]
            U[i][j] = (A[i][j] - sumu)/L[i][i]
            suml = 0.
            for k in range(0, i):
                suml += L[j][k] * U[k][i]
            L[j][i] = (A[j][i] - suml) / U[i][i]

        sumn = 0.
        for k in range(0, n - 1):
            sumn += L[n-1][k] * U[k][n-1]
        U[n - 1][n - 1] = A[n - 1][n - 1] - sumn
    
    if U[n - 1][n - 1] == 0:
        print('A = LU but A is singular')
    
    if np.array_equal(np.matmul(L, U), A):
        print('Factorization successful')
    else:
        print('Wrong factorization')
    return L, U

A = np.array(
    [
        [2.0, 1.0, 1.0],
        [1.0, 2.0, 1.0],
        [3.0, 1.0, 5.0]
    ]
)

b = [1, 2, 3]

L, U = LU_decomposition(A)
print('L: ')
print(L)
print('U: ')
print(U)
if L != None and U != None:
    y = matmul(inv(L), b)
    pprint.pprint(y)

    x = matmul(inv(U), y)
    pprint.pprint(x)

