import numpy as np

a=1
b=1
c=-5
d=-3


x = (a**2+2*a+2)+(d**2+2*d+2)-(a+d+2)**2
y = (a**2+2*a+2)*(d**2+2*d+2)

delta = x**2-4*y
print(delta)

print((-x+delta**0.5)/2)

M = np.array([[a,b],[c,d]])

print(M)

D = M.dot(M)+2*M+2*np.eye(2)

print(D)
print()
print(np.linalg.det(D))
