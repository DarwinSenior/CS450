from numpy import arange, float16
import numpy as np
a = float16(0.0)
b = float16(1000.0)
n = float16(1e4)
np.set_printoptions(formatter={'float': '{: 0.16f}'.format})
def add_method(a, b, n):
    h = (b-a)/n
    x = a
    xs = list()
    for k in range(int(n)+1):
        xs.append(x)
        x = x+h
    return xs

def mult_method(a, b, n):
    h = (b-a)/n
    xs = list()
    for k in range(int(n)+1):
        x = a+k*h
        xs.append(x)
    return xs

print "The x(1000) for addition method is: %f"%add_method(a, b, n)[-1]
print "The x(1000) for multiplication is: %f"%mult_method(a, b, n)[-1]