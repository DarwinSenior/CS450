import numpy as np
import numpy.linalg as la


def norm(x):
    return np.max(np.abs(x))

def normalise(x):
    return x/norm(x)

def shift(A, sigma):
    return A-np.eye(len(A))*sigma

def powerIter(A, x):
    while True:
        x = A.dot(x)
        x = x/norm(x)
        yield(x)
        
def rayleighQuotient(A, x):
    return x.dot(A).dot(x)/x.dot(x)

def estimate(A, x, iterator, error=0.0):
    # stop when it becomes stable, using infinity norm 
    v_prev = x
    countinggg = 0
    for v in iterator(A, x):
        if norm(v_prev-v)<=error or countinggg>100:
            return v, rayleighQuotient(A, v)
        else:
            v_prev = v
            countinggg += 1
            

A = np.array([[2.0, 3.0, 2.0],[10, 3, 4],[3, 6, 1]])
x = np.array([0.0, 0.0, 1.0])


x1, lambda1 = estimate(A, x, powerIter)
print x1, lambda1

def deflation(A, x1):
    v = x1.copy()
    v[0]-=la.norm(x1)
    H = np.eye(x1.size)-2*np.outer(v,v)/np.dot(v,v)
    return H.dot(A).dot(la.inv(H))[1:,1:]

A2 = deflation(A, x1)

x2, lambda2 = estimate(A2, np.array([1.0, 1.0]), powerIter)

print x2, lambda2

print la.eig(A)