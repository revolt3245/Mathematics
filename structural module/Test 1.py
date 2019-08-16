import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

theta = 0

fig, ax = plt.subplots(figsize = (12,12))

ax.set_xlim(-17, 17)
ax.set_ylim(-17, 17)

x = np.zeros((2,1))
y = np.zeros((2,1))

x[1] = np.cos(theta)
y[1] = np.sin(theta)

graphs, = plt.plot(x, y)

def animated(*args):
    global theta
    theta += np.pi/30
    
    x[1] = 15 * np.cos(theta)
    y[1] = 15 * np.sin(theta)
    
    graphs.set_data(x, y)
    return graphs, 

anim = animation.FuncAnimation(fig, func = animated, frames = 120, interval = 17, blit = True)

plt.show()