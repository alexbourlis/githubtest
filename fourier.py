from math import *
import matplotlib.pyplot as plt
from numpy.linalg import norm
import numpy as np

class MyFourierPlot:
    def __init__(self):
        self.fig = plt.figure()
        self.fig.suptitle("Fourier transform")
        self.ax1 = plt.subplot(221)
        self.ax1.set_title("function")
        self.ax1.axis([0,20,-2,2.5])
        self.ax1.grid(True)
        self.ax2 = plt.subplot(122, projection='polar')
        self.ax2.set_title("polar plot")
        self.ax2.axis([0,2*pi,0,2])
        self.ax3 = plt.subplot(223)
        self.ax3.set_title("spectrum")
        self.listcenter = np.empty(0)

    def _config(self):
        self.ax2.cla()
        self.ax3.cla()
        self.ax2.axis([0,2*pi,0,2.5])
        self.ax2.set_title("polar plot")
        self.ax3.set_title("spectrum")

    def actualize(self,theta,function,max):
        center = (function*np.exp(theta*1j)).sum()
        self.listcenter = np.append(self.listcenter,norm(center))

        self._config()
        self.ax2.plot(theta,function)
        self.ax2.plot(atan2(center.imag,center.real),3*norm(center)/max,'k.',markersize=10)
        
        listcenter_normalized = self.listcenter/self.listcenter.max()
        freqlist = freq[:len(self.listcenter)]
        self.ax3.plot(np.append(-freqlist[:0:-1],freqlist),np.append(listcenter_normalized[:0:-1],listcenter_normalized))
        
    

#--------functions definition-------------#
list1 = np.arange(0,50,0.01)
square = np.zeros(len(list1))
T = 0.5
square[int(10/0.01):int((10+T)/0.01)]=1
listsin = np.sin(list1)
listcos = np.cos(2*list1)
mode = "square"
match mode:
    case "sin":
        function = listsin+listcos+1 #the 1 term coresponds to a cosin function with frequency 0
        F = 2/pi
        max = 5000
    case "square":
        function = square
        F = 8
        max = 50
#--------end of definitions----------------#


fourier_plot = MyFourierPlot()
fourier_plot.ax1.plot(list1,function)

freq = np.linspace(0,F,200)

for i,f in enumerate(freq):
    theta = -2*pi*f*list1
    fourier_plot.actualize(theta,function,max)
    plt.pause(0.01)
    
plt.show()





