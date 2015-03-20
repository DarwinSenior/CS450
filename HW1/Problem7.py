from numpy import sqrt,pi,e,abs,arange

import matplotlib.pyplot as plt
def sterling(n):
    return sqrt(2*pi*n)*(n/e)**n

def fact(n):
    accum = 1
    for x in range(1,n+1):
        accum *= x
    return accum



def absolute_error(real, approx, x):
    return abs(real(x)-approx(x))

def relative_error(real, approx, x):
    return abs(real(x)-approx(x))/real(x)

fact_abs_error = lambda x: absolute_error(fact, sterling, x)
fact_rel_error = lambda x: relative_error(fact, sterling, x)


x = arange(1, 10, 1) # the testing value

plt.semilogy(x, map(fact_abs_error, x))
plt.title("Absolute value of stirling approximation")
plt.xlabel("n")
plt.ylabel("absolute value")
plt.savefig("p7_1.png")
plt.close()

plt.semilogy(x, map(fact_rel_error, x))
plt.title("relative value of stirling approximation")
plt.xlabel("n")
plt.ylabel("relative value")

plt.savefig("p7_2.png")
plt.close()