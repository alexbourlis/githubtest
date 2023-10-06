# SVD

import numpy as np
import numpy.linalg as npl

# Pimp my array
class MyArray(np.ndarray):

    def __new__(cls, input_array):
        obj = np.asarray(input_array).view(cls)
        #Complex Transpose a.k.a. adjoint
        obj.CT = np.conjugate(obj.T)
        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.CT = getattr(obj,'CT', None)

#some useful functions
def inner(a,b):
    return a.T.dot(np.conjugate(b))


a = np.array([
    [4],
    [-3],

])
a = MyArray(a)

A1 = np.concatenate([a,[[0],[0]]],axis=1)
A2 = np.array([
    [1,1,0],
    [0,0,1]
])
A3 = np.array([
    [1,9],
    [1,3],
    [6,1]
])

A=A3
print(A)

values,vectors = npl.eig(A.T@A)
print(f"Eigen values and vectors of A*A:\n{values}\n{vectors}")
list = np.squeeze(np.argwhere(values!=0),axis=1)
print(f"non 0 eigenvalues index: {list}")
C = vectors.T[list].T
positive_singular = np.sqrt(values[list])
print(f"positive singular values: {positive_singular}")
D = np.diag(positive_singular)
B = A.dot(C)/positive_singular
print()
print(f"B:\n{B}\nD:\n{D}\nC:\n{C}")
print(f"SVD correct:{(np.round(B@D@C.T,5)==np.round(A,5)).all()}")
print(f"SVD result:\n{np.round(B@D@C.T,3)}")
Aplus = C@npl.inv(D)@B.T
print(f"the pseudo inverse is:\n{np.round(Aplus,3)}")
print(np.round(Aplus@A,3))
print(np.round(A@Aplus,3))
#print(np.round(npl.inv(A.T@A)@A.T,3))#only if A is injective
#print(np.round(A.T@npl.inv(A@A.T),3))#only if A is surjective
print()
#built in SVD
#X = npl.svd(A,full_matrices=True)
#print((X[0]*X[1])@X[2])