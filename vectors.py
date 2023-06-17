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
	plt.xlim(border,-border)
	plt.ylim(-border,border)
	plt.show()


shape = (1,2)
v1 = np.array([2,9]).reshape(shape)
v2 = np.array([-2,4]).reshape(shape)
theta = 8*pi/7
M = np.array([[cos(theta),-sin(theta)],[sin(theta),cos(theta)]])
v3 = M.dot(v1.T).T
v4 = 1.3*M.T.dot(v3.T).T
#the transpose matrix on an orthogonal(orthonormal) matrix (matrix whose columns and rows are orthonormal) is equal to its inverse
M_inv = np.linalg.inv(M)
print("the inverse matrix: {:.100f}\n " .format(M_inv[0,1]-M.T[0,1]))
print("the transpose matrix: {:.100f}\n " .format(M.T[1,0]))

#V = np.concatenate([v1,v2,v3,v4])

v1 = np.array([3.77500024-3.77500029, 2.14056359-1.82378796])
vper = (np.array([[0,1],[-1,0]]).dot(v1)).tolist()
V = np.array([[3.91673542-3.76619143, 1.97378796- 1.88112803]])
norms = norm(V,axis=1).reshape((len(V),1))
axis_inverter = np.array([[0,1],[1,0]])
V = 10*V/norms
V = axis_inverter.dot(V.T).T

plot_vectors(V)

