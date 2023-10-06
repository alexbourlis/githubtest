import numpy as np
import matplotlib.pyplot as plt
from math import *
z1 = 4+3j
z = np.array([z1, z1*1j, z1*2j,z1*z1])

print(f"The real and imaginary part of z are {z.real} and {z.imag}")
norm = (z.real**2 + z.imag**2)**0.5
theta = np.arctan2(z.imag,z.real)
print(f"The norm and the phase of the number are {norm} and {theta}")
plt.polar(theta,norm,'k.',markersize=20)
plt.show()