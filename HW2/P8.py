import numpy as np
def H(n):
    return 1.0/np.array([[i+j+1 for i in range(n)] for j in range(n)])

def x(n):
    return np.ones((n,1))

def b(n):
    return H(n).dot(x(n))

def x_hat(n):
    return np.linalg.solve(H(n), b(n))

def r(n):
    return b(n)-H(n).dot(x_hat(n))

def error(n):
    return x(n)-x_hat(n)

def norm(v):
    return np.max(np.abs(v))

def k(n):
    return str(norm(error(n)))+" "+str(norm(r(n)))+" "+str(n)

def cond(n):
    return np.linalg.cond(H(n), np.inf)

if __name__ == '__main__':
	
	print "\n".join(map(k, range(1,20)))

	map(lambda n: cond(n+1)/cond(n), range(1, 10))
	


