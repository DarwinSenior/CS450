from numpy import sin, cos 
from numpy import arange
def f(x):
	return (1-cos(x))/(sin(x)*sin(x))
def g(x):
	return 1/(1+cos(x))
def approx(x):
	return 1/2.0+x*x/8.0

h= arange(0.0, 10.0, 1.0)
x= 10**(-h)
for line in zip(h, f(x), g(x), approx(x)):
	print "x: 10^-%d, f:%f, g:%f, approx:%f"%line