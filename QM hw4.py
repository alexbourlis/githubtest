import numpy as np
import matplotlib.pyplot as plt
from math import *
n = 247
L =  ceil(np.log2(n))	#number of lower qbits
t = 2*L + 1 

coprimes = [i for i in range(2,n) if gcd(i,n) == 1]

print(len(coprimes))

a = None 	# crapy guess
for candidate in coprimes:
	if [(candidate**i)%n for i in range(0,4)] == [(candidate**i)%n for i in range(4,8)]:
		a = candidate
		break

print(a)
print(np.array([(a**i)%n for i in range(1000)]))


k = np.arange(2**15)
l = np.arange(2**13)
coef = 1/np.sqrt(2**32)*np.exp(1j*pi*np.outer(l,k)/2**14).sum(axis=1)

#plt.plot(l,np.sqrt(coef.real**2 + coef.imag**2))
#plt.show()