import numpy as np
import matplotlib.pyplot as plt

def Scatter(*parameter, dtype = 'c'):
    if(dtype == 'c'):
        return parameter[0].real, parameter[0].imag
    elif(dtype == 'sf'):
        value = parameter[0](parameter[1])
        return value.real, value. imag
    elif(dtype == 'df'):
        value = parameter[0](parameter[1], parameter[2])
        return value.real, value.imag

def Mul(a, b):
    return a * b

def isin(a):
    value = np.sin(a.real)*np.cosh(a.imag) + 1j*np.cos(a.real)*np.cosh(a.imag)
    return value

def icos(a):
    value = np.cos(a.real)*np.cosh(a.imag) - 1j*np.sin(a.real)*np.sinh(a.imag)
    return value

def iexp(a):
    rvalue = np.exp(a.real)*np.cos(a.imag)
    ivalue = np.exp(a.real)*np.sin(a.imag)
    return rvalue + 1j*ivalue

def frac(a):
    return 1/a

def itself(a):
    return a

def comb(*p, dtype = 'sp'):
    if(dtype == 'sp'):
        return p[0](p[1](p[2]))
    elif(dtype == 'dp'):
        return p[0](p[1](p[3]), p[2](p[3]))