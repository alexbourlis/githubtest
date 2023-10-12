import numpy as np
from math import *

class Vector:
    def __init__(self,nparray):
    	self.DIM = 8
    	self.ket = nparray.reshape((self.DIM,1))

    def __str__(self): 
    	s = ""
    	if (self.ket == np.zeros((self.DIM,1))).all():
    		return '0'
    	first = True
    	for i in range(self.DIM):
    		if self.ket[i][0] != 0:
    			if first == False:
    				s = s + f' + ({np.round(self.ket[i][0],2)})B{i}'
    			else:
    				s = s + f'({np.round(self.ket[i][0],2)})B{i}'
    			first = False
    	return s

class fket:
    def __init__(self,nparray,mode = 0):
    	self.DIM = 8
    	self.ket = nparray.reshape((self.DIM,1))
    	self.mode = mode

    def __str__(self): 
    	s = ""
    	if (self.ket == np.zeros((self.DIM,1))).all():
    		return '0'
    	first = True
    	for i in range(self.DIM):
    		if self.ket[i][0] != 0:
    			ket_value = f'|{floor(i/4)}{floor((i%4)/2)}{i%2}>' if self.mode == 0 else f'|{i}>'
    			if first == False:
    				s = s + f' + ({np.round(self.ket[i][0],2)})' + ket_value
    			else:
    				s = s + f'({np.round(self.ket[i][0],2)})' + ket_value
    			first = False
    	return s

def ket(s):
	if type(s) == type(str()):
		s = int(s[0])*4+int(s[1])*2+int(s[2])
	return np.eye(8)[s].reshape((8,1))

def truth_table(M,mode = 0):
	s = 'input  |  output\nx2x1x0 | x2x1x0\n'
	if mode == 0:
		for i in range(8):
			k = np.where(M.dot(ket(i)) != 0)[0][0]
			s = s + f'  {floor(i/4)}{floor((i%4)/2)}{i%2}  |  {floor(k/4)}{floor((k%4)/2)}{k%2}\n'
	else:
		for i in range(8):
			k = np.where(M.dot(ket(i)) != 0)[0][0]
			s = s + f'  {i}  |  {k}\n'

	print(s)

U = np.array([
	[1,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,1],
	[0,1,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,1,0]
])
#toffofl gate on x0
toffx0 = np.array([
	[1,0,0,0,0,0,0,0],
	[0,1,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,0,1],
	[0,0,0,0,0,0,1,0]
])
#toffoli gate on x1
toffx1 = np.array([
	[1,0,0,0,0,0,0,0],
	[0,1,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,0,0,0,1],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,1,0,0]
])
#toffoli gate on x2
toffx2 = np.array([
	[1,0,0,0,0,0,0,0],
	[0,1,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,0,0,0,0,0,1],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,1,0,0,0,0]
])
#zero-controled toffoli on x0
zctoffx0 = np.array([
	[0,1,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,0,0,1,0],
	[0,0,0,0,0,0,0,1]
])
#NOT gate
X = np.array([
	[0,1],
	[1,0]
])

I = np.eye(2)

# Controlled NOT Gate from x0 to x1
CNOT01 = np.array([
	[1,0,0,0],
	[0,0,0,1],
	[0,0,1,0],
	[0,1,0,0]
])
# Controlled NOT Gate from x1 to x0
CNOT10 = np.array([
	[1,0,0,0],
	[0,1,0,0],
	[0,0,0,1],
	[0,0,1,0]
])

CNOT20 = np.array([
	[1,0,0,0,0,0,0,0],
	[0,1,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0],
	[0,0,0,1,0,0,0,0],
	[0,0,0,0,0,1,0,0],
	[0,0,0,0,1,0,0,0],
	[0,0,0,0,0,0,0,1],
	[0,0,0,0,0,0,1,0]
])

Up = np.kron(I,np.kron(I,X))@zctoffx0@np.kron(I,CNOT01)@toffx2
Zc = np.kron(I,np.kron(I,X))@toffx0@CNOT20@np.kron(I,CNOT10)
print(Zc)

print((Up == U).all())


v = ket(4)+ket(2)+ket(7)

print(fket(zctoffx0.dot(ket('111')),mode = 1))

#truth_table(CNOT20,mode=1)
