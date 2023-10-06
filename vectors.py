import numpy as np
from numpy import sin,cos,pi
from numpy.linalg import norm
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def plot_vectors(V_list):
	border = 20
	origin = np.zeros((2,len(V_list)))
	ind = 10
	colors = [*mcolors.CSS4_COLORS][ind:ind+len(V_list)]

	plt.quiver(*origin,V_list[:,0],V_list[:,1],color=colors,angles= "xy", scale_units="xy",scale= 1)
	plt.axis("equal")
	plt.xlim(-border,border)
	plt.ylim(-border,border)
	plt.show()


theta = pi/4
shape = (1,2)
v1 = 5*np.array([-sin(theta/2),cos(theta/2)]).reshape(shape)
v1 = np.array([3,10]).reshape(shape)

M = np.array([[cos(theta),sin(theta)],[sin(theta),-cos(theta)]])
M2 = M.dot(M)
M3 = M.dot(M2)
v2 = M.dot(v1.T).T
#the transpose matrix on an orthogonal(orthonormal) matrix (matrix whose columns and rows are orthonormal) is equal to its inverse

V = np.concatenate([v1,v2])


plot_vectors(V)

