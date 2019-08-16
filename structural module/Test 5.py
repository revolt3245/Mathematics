import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def PositionVec(Base, Plength, Alength):
    X = np.zeros((2,1))
    X[0] = (Plength**2 - Alength**2 + Base**2)/(2*Base)
    X[1] = np.sqrt(Plength**2 - X[0]**2)
    return X

def NewPointVector(Pivot, Arm, Plength, Alength):
    Pvec = Arm - Pivot
    Base = lin.norm(Pvec)
    Pvec /= Base
    
    #Position Vector in transformed domain
    PosVec = PositionVec(Base, Plength, Alength)
    
    #Rotation Tensor
    Pvec90 = np.roll(Pvec, 1)
    Pvec90[0] = -Pvec90[0]
    
    RotTen = np.hstack([Pvec, Pvec90])
    
    return np.matmul(RotTen, PosVec) + Pivot

theta = 0

fig, ax = plt.subplots(figsize = (12,12))

ax.set_xlim(-150, 50)
ax.set_ylim(-100, 100)

Points = np.zeros((2,8))

graphs = [ax.plot([], [], color = 'C0')[0] for i in range(6)]

'''
Seqence - (PivotInd, ArmInd, PivotLen, Armlen)
'''
Sequence = [(1,2,41.5,50.0), (2,1,61.9,39.3),
           (1,3,40.1,55.8), (4,5,36.7,39.4),
           (4,6,49.0,65.7)]

Points[:,0] = [0, 7.8]
Points[:,1] = [-38.0, 0]

def Animated(*args):
    global theta
    theta += np.pi/30
    
    Points[:,2] = Points[:,0] + [np.cos(theta) * 15, np.sin(theta) * 15]
    
    graphs[0].set_data(Points[0,(0,2)], Points[1,(0,2)])
    
    for i in range(5):
        PInd, AInd, Plen, Alen = Sequence[i]
        
        NP = NewPointVector(Points[:,PInd].reshape(-1,1), Points[:,AInd].reshape(-1,1), Plen, Alen)
        Points[:,i+3] = NP.reshape(-1)
        graphs[i+1].set_data(Points[0,(PInd, i+3, AInd)], Points[1,(PInd, i+3, AInd)])
    
    return graphs

anim = animation.FuncAnimation(fig, func = Animated, frames = 900, interval = 17, blit = True)

#anim.save("Theo-Jansen's Linkage.mp4", fps = 60, dpi = 72)

plt.show()