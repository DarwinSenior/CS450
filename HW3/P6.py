import numpy as np

def norm(x):
    return np.max(np.abs(x))

def shift(A, sigma):
    return A-np.eye(len(A))*sigma


def inversePowerIter(A, x):
    while True:
        x = np.linalg.solve(A, x)
        x = x/norm(x)
        yield(x)

A = np.array([[6.0, 2.0, 1.0],[2.0, 3.0, 1.0],[1.0, 1.0, 1.0]])
x = np.array([0.0, 0.0, 1.0])
        
def rayleighQuotient(A, x):
    return x.dot(A).dot(x)/x.dot(x)

def estimating(A, x, iterator, error=0.0):
    # stop when it becomes stable, using infinity norm 
    v_prev = x
    for v in iterator(A, x):
        if norm(v_prev-v)<=error:
            return v, rayleighQuotient(A, v)
        else:
            v_prev = v

print estimating(A, x, inversePowerIter)

import numpy.linalg as la
print la.eigvalsh(A)

def rayleighIter(A, x):
    while True:
        sigma = rayleighQuotient(A, x)
        x = np.linalg.solve(shift(A, sigma), x)
        x = x/norm(x)
        yield(x)
        
print estimating(A, x, rayleighIter)