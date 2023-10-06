from math import *

a,b,c = [pi/3,pi/3,pi/3]

C = acos((cos(c)-cos(a)*cos(b))/(sin(a)*sin(b)))
L1 = 3*C-pi
print(L1)

c = pi/2
C = acos((cos(c)-cos(a)*cos(b))/(sin(a)*sin(b)))
A = asin(sin(a)*sin(C)/sin(c))
L2 = C+2*A-pi

Vatoms = 2*4*L1+6*2*L2
Vmesh = 6*sqrt(8)

Comp = Vatoms/Vmesh

print(Comp)

