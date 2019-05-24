import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots(figsize = (12, 12))

ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

graphs, = ax.plot([], [])

theta = np.zeros((2,1))
dtheta = np.zeros((2,1))

theta[:,0] = [np.pi/2, np.pi/2]

RK = np.zeros((2,4))
dRK = np.zeros((2,4))

def RKGenerator(theta, dtheta, m_tick):
    RK = np.zeros((2,4))
    dRK = np.zeros((2,4))
    AccTensor = np.zeros((2,2))
    AccBias = np.zeros((2,1))
    AccVec = np.zeros((2,1))
    
    K = theta
    dK = dtheta
    
    for i in range(4):
        if i == 0:
            tick = 0
        elif i == 3:
            tick = m_tick
        else:
            tick = m_tick/2
            
        K[:,0] = theta[:,0]+tick*RK[:,i-1]
        dK[:,0] = dtheta[:,0]+tick*dRK[:,i-1]
        RK[:, i] = dK[:, 0]
        AccTensor[:,:] = [[2, np.cos(K[1,0]-K[0,0])],
                 [np.cos(K[1,0]-K[0,0]), 1]]
        AccBias[:, 0] = [np.sin(K[1,0]-K[0,0])*dK[1,0]**2 - 20*np.sin(K[0,0]),
               -np.sin(K[1,0]-K[0,0])*dK[0,0]**2 - 10*np.sin(K[1,0])]
        AccVec = np.matmul(lin.inv(AccTensor), AccBias)
        dRK[:,i] = AccVec[:,0]
        
    return RK, dRK

#solve equation
def animated(*args):
    global theta, dtheta
    global RK
    global dRK
    
    tick = 1/3000
    
    XUpdate = 0
    YUpdate = 0
    for i in range(100):
        RK, dRK = RKGenerator(theta, dtheta, tick)
        ThetaUpdate = RK[:,0] + 2*RK[:,1] + 2*RK[:,2] + RK[:,3]
        dThetaUpdate = dRK[:,0] + 2*dRK[:,1] + 2*dRK[:,2] + dRK[:,3]
        
        theta[:,0] += tick*ThetaUpdate/6
        dtheta[:,0] += tick*dThetaUpdate/6
        
    xdata = [0]
    ydata = [0]
    
    for i in range(2):
        XUpdate += np.sin(theta[i,0])
        YUpdate -= np.cos(theta[i,0])
        xdata.append(XUpdate)
        ydata.append(YUpdate)
        
    graphs.set_data(xdata, ydata)
    
    return graphs,

ani = animation.FuncAnimation(fig, func = animated, frames = 900, interval = 5, blit = True)

ani.save('DoublePendulum.mp4', fps = 30)
plt.show()