import numpy as np
from math import *
import matplotlib.pyplot as plt
from matplotlib import cm

def csin(z):
	return (np.exp(1j*z)-np.exp(-1j*z))/2j

def casin(z):
	return -1j*np.log(1j*z+np.emath.sqrt(1-z**2))

x = np.arange(-10,10,0.1)

X = np.round(np.outer(x,np.ones(np.size(x))),1)
Y = X.copy().T

Z = np.real(casin(X+Y*1j))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
#ax = plt.axes(projection = '3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
boundary = 10
ax.set_xlim([-boundary,boundary])
ax.set_ylim([-boundary,boundary])
ax.set_zlim([-boundary,boundary])
        
x = [20,0,0]
y = [0,20,0]
z = [0,0,20]
xyz_f = np.array([x,y,z])
xyz_i = -xyz_f/2
ax.quiver(*xyz_i,*xyz_f,color='k',arrow_length_ratio=0.1)

cmap = cm.viridis
norm = plt.Normalize(Z.min(), Z.max())
ax.plot_surface(X,Y,Z,color='b',alpha=0.6,rstride=1, cstride=1,facecolors=cmap(norm(Z)),linewidth=0)
m = cm.ScalarMappable(cmap=cmap, norm=norm)
m.set_array(Z)
fig.colorbar(m)

plt.show()