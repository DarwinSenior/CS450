import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt
# import seaborn


data = np.array([[-1.02494, -0.389269],
[-0.949898, -0.322894],
[-0.866114, -0.265256],
[-0.773392, -0.216557],
[-0.671372, -0.177152],
[-0.559524, -0.147582],
[-0.437067, -0.128618],
[-0.302909, -0.121353],
[-0.155493, -0.127348],
[-0.007464, -0.148885]])

X = data[:,0]
Y = data[:,1]

def lstsq_solve(A, x):
    Q,R = la.qr(A)
    x = la.solve(R, Q.T.dot(b))
    r = A.dot(x)-b
    return x, la.norm(r)


def plot1(para):
    x = np.linspace(-1, 0)
    a,b,c,d,e = para
    A = a
    B = b*x+d
    C = c*x+e-x**2
    y = (-B+np.sqrt(B**2-4*A*C))/(2*A)
#     pyplot.plot(x,y)
    y = (-B-np.sqrt(B**2-4*A*C))/(2*A)
    plt.plot(x,y, label="model1")

def plot2(para):
    x = np.linspace(-1, 0)
    d, e = para
    y = (x**2-e)/d
    plt.plot(x,y, label="model2")

plt.plot(X, Y, label="data")

# first model x^2=ay^2+bxy+cx+dy+e
A = np.array([Y*Y, X*Y, X, Y, np.ones(len(X))]).T
b = X*X

para, r = lstsq_solve(A, b)

plot1(para)
print r

A = np.array([Y,np.ones(len(X))]).T

b = X*X

para, r = lstsq_solve(A, b)

plot2(para)
print r


plt.legend()
plt.xlabel("x value")
plt.ylabel("y value")
plt.savefig("P7.png")