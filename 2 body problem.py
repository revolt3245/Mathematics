import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
import matplotlib.animation as animation

'''
Mass Unit - Solar Mass
Distance Unit - AU
time unit - Day

Gravitational Weight - 1.72e-2

Set Mass of particles all 1SM
'''

X = np.zeros((2,1))
dX = np.zeros((2,1))

X[:,0] = [1, -1]

RK = np.zeros((4,2,1))
dRK = np.zeros((4,2,1))

def DenominatorFactor(X):
    factor = 0.0001
    return np.sqrt(X**2 + factor**2)

def RKGenerator(X, dX, m_tick):
    RK = np.zeros((4,2,1))
    dRK = np.zeros((4,2,1))
    K = np.zeros((2,1))
    dK = np.zeros((2,1))
    
    gw = 1.72e-2
    
    for i in range(4):
        if i == 0:
            tick = 0
        elif i == 3:
            tick = m_tick
        else:
            tick = m_tick/2
            
        K = X + tick*RK[i-1]
        dK = dX + tick*dRK[i-1]
        
        RK[i] = dK
        dRKUpdate =  K * gw**2/(DenominatorFactor(K)**3)
        dRK[i] = dRKUpdate
    return RK, dRK
