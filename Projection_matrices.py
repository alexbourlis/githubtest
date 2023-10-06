# Projection matrices
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


#project onto [4 -3] 2x2

a = np.array([
    [4],
    [-3]
])
a = MyArray(a)

print("the projection matrix is:")
#formula T(T*T)^(-1)T*
P = a@npl.inv(a.CT@a)@a.CT
print(P)
#simplified solution for a real line
#print(a.dot(a.T)/inner(a,a))
