from numpy import abs
def finiteDiff(f, x, h):
    return (f(x+h)-f(x))/h

def error(f, df, x, h):
    return abs(finiteDiff(f, x, h)-df(x))

from numpy import sin, cos, minimum, arange
from matplotlib import pyplot as plt
# import seaborn

dcos = lambda x: -sin(x)

sin_error = lambda h: error(cos, dcos, 1, h)

k = arange(0, 16, 1) # the testing value
h = 10.0**(-k)

sin_errors = sin_error(h)
plt.title("Error for finite differnece formula respect to h")
plt.xlabel("h")
plt.ylabel("error")
plt.loglog(h, sin_errors)
plt.savefig("p6_1.png")
plt.close()

print "The smallest error is %e"%min(sin_errors)

def finiteDiff4(f, x, h):
    return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)



k = arange(0, 16, 1) # the testing value
h = 10.0**(-k)

sin_error4 = lambda h: abs(finiteDiff4(cos, 1, h)-dcos(1))

sin_errors4 = sin_error4(h)
plt.loglog(h, sin_errors4)
plt.title("Error for finite differnece formula respect to h")
plt.xlabel("h")
plt.ylabel("error")

plt.savefig("p6_2.png")
plt.close()

print "The smallest error is %e"%min(sin_errors4)
