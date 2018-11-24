import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize = (12,6))
fig.suptitle("Laplace inverse transform", fontsize = 16)

ax1 = fig.add_subplot(3,2,1)
ax2 = fig.add_subplot(1,2,2)
ax3 = fig.add_subplot(3,2,3)
ax4 = fig.add_subplot(3,2,5)

ax1.title.set_text("S domain")
ax2.title.set_text("t domain")
def iexp(s):
    real = s.real
    imag = s.imag
    
    res = np.exp(real)*(np.cos(imag) + 1j * np.sin(imag))
    
    return res

sreal = np.ones(160000)
simag = np.arange(-800*np.pi, 800*np.pi, 0.01*np.pi)
Func = np.zeros(1400, dtype = complex)
T = np.arange(-7, 7, 0.01)

s = sreal + 1j * simag

for complexfreq in s:
    if(complexfreq != 0):
        Func += iexp(complexfreq*T)/((complexfreq**2) + 1) * 0.005
    
S_real = np.linspace(-1, 1, 50)
S_imag = np.linspace(-2, 2, 100)

R, I = np.meshgrid(S_real, S_imag)
Z_R = (R**2 - I**2 +1)/((R**2 - I**2 +1)**2 + 4*(R**2)*(I**2))
Z_len = 1/np.sqrt((R**2 - I**2 +1)**2 + 4*(R**2)*(I**2))
Z_I = (4*(R**2)*(I**2))/((R**2 - I**2 + 1)**2 + 4*(R**2)*(I**2))

ax1.contourf(R, I, Z_len)
ax1.contour(R, I, Z_len, color = 'black')
ax2.plot(T, Func.real)
ax3.contourf(R, I, Z_R)
ax4.contourf(R, I, Z_I)
