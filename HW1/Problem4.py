import numpy as np

def machine_percision_test(p, b, data_type):
    one = data_type(1) #test against
    return one+(b**(-p))!=1 # fl(1+epsilon)!=fl(1)

def machine_undeflow_test(p, b, data_type):
    one = data_type(1) # test against
    return b**(-p)!=0

def epsilon_mach(data_type):
    p = 1
    b = data_type(2) # assume base of 2
    while(machine_percision_test(p, b, data_type)):
        p += 1
    return p

def UFL(data_type):
    p = 1
    b = data_type(2) # assume base of 2
    while(machine_undeflow_test(p, b, data_type)):
        p += 1
    return p-1


print "The epsilon_machine for float 64 is 2^{-%d}, the UFL is 2^{-%d}"%(epsilon_mach(np.float64), UFL(np.float64))
print "The epsilon_machine for float 128 is 2^{-%d}, the UFL is 2^{-%d}"%(epsilon_mach(np.float128), UFL(np.float128))