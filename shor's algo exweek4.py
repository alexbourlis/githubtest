import numpy as np
from math import *
import matplotlib.pyplot as plt

n = 15 					#product of primes

L =  ceil(np.log2(n))	#number of lower qbits
t = 2*L + 1 			#number of top qbits
#t=4
x = range(0,2**t)		#all different values for each combinations of upper qbits
a = 4 					#crapy guess

Lout = np.array([(a**i)%n for i in x])

eigenvalue = 4
v = Lout == eigenvalue
v = v/np.sqrt((v**2).sum())			#v normalized
print(v)

print(Lout)

#k = np.arange(8)
#l = np.arange(16)

#coef = 1/np.sqrt(2**7)*np.exp(1j*4*pi*np.outer(l,k)/16).sum(axis=1)
#	
#print(np.round(coef,3))
##print(m)

QFT = 1/np.sqrt(2**t)*np.exp(2j*np.pi/(2**t)*np.outer(np.arange(2**t),np.arange(2**t)))
#v = 1/np.sqrt(2**3)*np.array([1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0])

print(np.round(QFT.dot(v),3))

plt.plot(x,np.sqrt(QFT.dot(v).real**2+QFT.dot(v).imag**2))#np.sqrt(coef.real**2 + coef.imag**2))
plt.show()