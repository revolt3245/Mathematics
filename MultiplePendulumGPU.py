import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig, ax = plt.subplots(figsize = (12,12))

n = int(input("number of pendulum : "))

ax.set_xlim(-float(n)-0.2,float(n)+0.2)
ax.set_ylim(-float(n)-0.2,float(n)+0.2)

graphs, = ax.plot([], [])

theta = np.ones((n,1))
dtheta = np.zeros((n,1))

theta *= np.pi/2

RK = np.zeros((n,4))
dRK = np.zeros((n,4))

Gain = np.zeros((n,n))
dGain = np.identity(n)

for i in range(n):
    for j in range(n):
        Gain[i,j] = n - max(i,j)

dGain *= Gain
def AccTBGenerator(theta,dtheta, n):
    global Gain, dGain
    MulVec = np.ones((1,n))
    thetaArr = np.matmul(theta,MulVec)
    thetaArr = thetaArr.transpose() - thetaArr
    AccTensor = np.cos(thetaArr)*Gain
    
    dthetaTensor = np.sin(thetaArr) * Gain
    dthetaVec = np.matmul(dthetaTensor, dtheta**2)
    SinVec = np.matmul(dGain, np.sin(theta))
    AccChar = dthetaVec - 10*SinVec
    
    return AccTensor, AccChar

def RKGenerator(theta, dtheta, m_tick, n):
    RK = np.zeros((n,4))
    dRK = np.zeros((n,4))
    AccVec = np.zeros((n,1))
    
    K = np.zeros((n,1))
    dK = np.zeros((n,1))
    
    for i in range(4):
        if i == 0:
            tick = 0
        elif i == 3:
            tick = m_tick
        else:
            tick = m_tick/2
            
        K[:,0] = theta[:,0] + tick*RK[:,i-1]
        dK[:,0] = dtheta[:,0] + tick*dRK[:,i-1]
        
        RK[:,i] = dK[:,0]
        AccTensor, AccChar = AccTBGenerator(K,dK, n)
        AccVec = np.matmul(lin.inv(AccTensor), AccChar)
        dRK[:,i] = AccVec[:,0]
        
    return RK, dRK

def animated(*args):
    global theta, dtheta
    global RK
    global dRK
    
    tick = 1/3000
    
    XUpdate = 0
    YUpdate = 0
    for i in range(100):
        RK, dRK = RKGenerator(theta, dtheta, tick, n)
        ThetaUpdate = RK[:,0] + 2*RK[:,1] + 2*RK[:,2] + RK[:,3]
        dThetaUpdate = dRK[:,0] + 2*dRK[:,1] + 2*dRK[:,2] + dRK[:,3]
        
        theta[:,0] += tick*ThetaUpdate/6
        dtheta[:,0] += tick*dThetaUpdate/6
        
    xdata = [0]
    ydata = [0]
    
    for i in range(n):
        XUpdate += np.sin(theta[i,0])
        YUpdate -= np.cos(theta[i,0])
        xdata.append(XUpdate)
        ydata.append(YUpdate)
        
    graphs.set_data(xdata, ydata)
    
    return graphs,

ani = animation.FuncAnimation(fig, func = animated, frames = 18000, interval = 5, blit = True)

'''
start_time = time.time()
ani.save('{}-tuple Pendulum with revised method.mp4'.format(n), fps = 30)
end_time = time.time()

print("{}s".format(end_time - start_time))
'''
plt.show()