import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

class My3Dvec:
    def __init__(self,axis=True,sphere=True):
        self.fig = plt.figure()
        self.ax = plt.axes(projection = '3d')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_xlim([-10,10])
        self.ax.set_ylim([-10,10])
        self.ax.set_zlim([-10,10])
        if axis: self._plot_axis()
        if sphere: self._plot_sphere()
    def _plot_axis(self):
        x = [20,0,0]
        y = [0,20,0]
        z = [0,0,20]
        xyz_f = np.array([x,y,z])
        xyz_i = -xyz_f/2
        self.ax.quiver(*xyz_i,*xyz_f,color='k',arrow_length_ratio=0.1)
    def _plot_sphere(self):
        radius = 4
        a = np.linspace(0,2*np.pi,200)
        b= np.linspace(0,np.pi,200)
        x = np.outer(np.cos(a),np.sin(b))*radius
        y = np.outer(np.sin(a), np.sin(b))*radius
        z = np.outer(np.ones(np.size(a)),np.cos(b))*radius
        self.ax.plot_surface(x,y,z,color='b',alpha=0.2)

    def plot_vectors(self,origin,V_list):
        ind = 10
        colors = [*mcolors.CSS4_COLORS][ind:ind+len(V_list)]
        self.ax.quiver(*origin,*V_list.T,color=colors,arrow_length_ratio=0.1)

plot_3D = My3Dvec()

u = [2,3,1]
v = [0,5,4]
q = [7,-8,10]
V_list = np.array([u,v,q])
origin = np.zeros((3,len(V_list)))

plot_3D.plot_vectors(origin,V_list)


plt.show()