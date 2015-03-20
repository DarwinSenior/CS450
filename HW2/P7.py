import numpy as np

def LU(M):
    size = M.shape[0]
    L = np.eye(size)
    U = np.copy(M)
    for i in range(size-1):
        # eliminating
        coeff = (U[i+1:,i]/U[i,i]).reshape(size-i-1,1)
        U[i+1:,i:] -= coeff.dot(U[i,i:].reshape((1,size-i)))
        L[i+1:,i] = coeff.reshape((size-i-1,))
    return L, U

def backward_sub(U, b):
    size = U.shape[0]
    x = np.zeros(size)
    for i in range(size):
        k = size-i-1
        x[k] = (b[k]-U[k,k+1:].dot(x[k+1:]))/U[k,k]
    return x

def forward_sub(L, b):
    size = L.shape[0]
    x = np.zeros(size)
    for i in range(size):
        x[i] = (b[i]-L[i,:i].dot(x[:i]))/L[i,i]
    return x

def solve(A, b):
    L, U = LU(A)
    Ux = forward_sub(L, b)
    x = backward_sub(U, Ux)
    return x

def solveLU(L, U, b):
    Ux = forward_sub(L, b)
    x = backward_sub(U, Ux)
    return x

def solveUpdate(L, U, x, u, v):
    z = solveLU(L, U, u)
    y = x+v.dot(x)/(1-v.dot(z))*z
    return y

if __name__ == '__main__':
	A = np.array([[2, 4, -2], [4, 9, -3], [-2, -1, 7]], dtype=np.float)
	b = np.array([2, 8, 10], dtype=np.float)
	L, U = LU(A)
	x = solveLU(L, U, b)
	print x # it is python2 and the reason to factorise is for the next question
	print np.linalg.solve(A, b)

	u = np.array([1, 0, 0], dtype=np.float)
	v = np.array([0, 2, 0], dtype=np.float)
	y = solveUpdate(L, U, x, u, v)
	A_prim = np.array([[2, 2, -2], [4, 9, -3], [-2, -1, 7]], dtype=np.float)
	print y
	print np.linalg.solve(A_prim, b)