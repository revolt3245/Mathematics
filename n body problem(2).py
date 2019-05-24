import numpy as np
import numpy.linalg as lin
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

'''
Mass Unit - Solar Mass
Distance Unit - AU
time unit - Day

Gravitational Weight - 1.72e-2

Set Mass of particles all 1SM
'''

n = int(input("number of bodies : "))

theta = np.random.rand(n)
phi = np.random.rand(n)

theta *= 2*np.pi
phi *= np.pi

X = np.zeros((n,1,3,1))

X[:,:,0,:] = (0.1*np.sin(theta)*np.cos(phi)).reshape(n,1,1)
X[:,:,1,:] = (0.1*np.sin(theta)*np.sin(phi)).reshape(n,1,1)
X[:,:,2,:] = (0.1*np.cos(theta)).reshape(n,1,1)

dX = np.zeros((n,1,3,1))

def DistanceTensorGen(X):
    MulVec = np.zeros((1,n,3,3))
    disfactor = np.ones((n,n))
    disfactor *= 1e-2
    
    for i in range(3):
        MulVec[:,:,i,i] = np.ones((1,n))
    
    VecTensor = np.matmul(MulVec, X)
    
    VecTensor -= VecTensor.transpose((1,0,2,3))
    
    DisTensor = lin.norm(VecTensor, axis = (2,3))
    DisTensor = np.sqrt(DisTensor**2 + disfactor**2)
    
    return -VecTensor, DisTensor

def RKGenerator(X, dX, m_tick):
    RK = np.zeros((n,4,3,1))
    dRK = np.zeros((n,4,3,1))
    
    K = np.zeros((n,1,3,1))
    dK = np.zeros((n,1,3,1))
    
    MulVec = np.ones((3,1,n,1))
    
    gm = 1.72e-2
    
    for i in range(4):
        if i == 0:
            tick = 0
        elif i == 3:
            tick = m_tick
        else:
            tick = m_tick/2
            
        K[:,0,:,:] = X[:,0,:,:] + tick*RK[:,i-1,:,:]
        dK[:,0,:,:] = dX[:,0,:,:] + tick*dRK[:,i-1,:,:]
        
        RK[:,i,:,:] = dK[:,0,:,:]
        Vec, Dis = DistanceTensorGen(K)
        AccTensor = Vec * (gm**2)/(Dis[:,:,None,None]**3)
        Temp = np.matmul(AccTensor.transpose((2,3,0,1)), MulVec)
        dRK[:,i,:,:] = Temp.transpose((2,3,0,1)).reshape(n,3,1)
    return RK, dRK

def updatePosition(tick):
    global X, dX
    RK, dRK = RKGenerator(X, dX, tick)
    X[:,0,:,:] += (RK[:,0,:,:] + 2*RK[:,1,:,:] + 2*RK[:,2,:,:] + RK[:,3,:,:])/6*tick
    dX[:,0,:,:] += (dRK[:,0,:,:] + 2*dRK[:,1,:,:] + 2*dRK[:,2,:,:] + dRK[:,3,:,:])/6*tick

def drawPoint():
    global X
    Xpoint = X.reshape(n,3)
    glBegin(GL_POINTS)
    for i in Xpoint:
        glVertex3fv(i*10)
    glEnd()
    
def myOpenGL():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -7)
    
    while True:
        for i in range(10):
            updatePosition(1/1000)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        drawPoint()
        pygame.display.flip()
        pygame.time.wait(10)
        
myOpenGL()
