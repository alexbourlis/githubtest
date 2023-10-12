import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from math import *
def csin(z):
	return (np.exp(1j*z)-np.exp(-1j*z))/2j
def casin(z):
	return -1j*np.log(1j*z+np.emath.sqrt(1-z**2))
# Create the X, Y, and Z coordinate arrays.
boundary = 2 
x = np.linspace(-boundary, boundary, 101)
y = np.linspace(-boundary, boundary, 101)
X, Y = np.meshgrid(x, y)
#Z = np.sin(np.sqrt(X**2 + Y**2))
Zp = np.real(casin(X+Y*1j))
Z = np.imag(casin(X+Y*1j))
# Create a surface plot and projected filled contour plot under it.
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
# Select Colormap
cmap = cm.viridis
# Norm for color mapping
norm = plt.Normalize(Zp.min(), Zp.max())
# Plot surface with color mapping
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, facecolors=cmap(norm(Zp)), alpha=0.9, linewidth=0)
# Add a color bar which maps values to colors
m = cm.ScalarMappable(cmap=cmap, norm=norm)
m.set_array(Zp)
fig.colorbar(m)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()