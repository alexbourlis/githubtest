import numpy as np
from numpy.linalg import *
#import torch


M = np.array([[6,0,0],[0,7,1],[0,0,7]])
M = np.array([[0,1],[1,1]])

print("eigen values: ", eig(M)[0])
print("eigen vectors:\n ", np.array_str(eig(M)[1].T, precision=3, suppress_small=True),"\n")

#N = torch.tensor([[1.,1.],[0.,1.]])
#
#print(torch.linalg.eig(N))
#
#print(N.numpy().dot([0,1]))


