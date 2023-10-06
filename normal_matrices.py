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

# An normal matrix

def inner(a,b):
    return a.dot(np.conjugate(b.T))

M1 = np.array([
    [1,1,0],
    [0,1,1],
    [1,0,1]
])

# For the matrix M2 it is interesting to notice that the 1st and 3rd eigenvectors aren't orthogonal.
# They have the same eigenvalue thus orthogonality isn't guaranteed, even though the matrix is unitary
M2 = np.array([
    [1,  1,  1,   1],
    [1, 1j, -1, -1j],
    [1, -1,  1,  -1],
    [1,-1j, -1,  1j]
])

M = MyArray(M2/2)#When dividing M2 by 2 it becomes an isometry
normal = (M.dot(M.CT) == M.CT.dot(M)).all()

print(f"The matrix is normal: {normal}\n")
print(f"the matrix times its adjoint is:\n\n {M.CT.dot(M)}\n")

#Eigen vectors and values
values,vectors = npl.eig(M)
print("Eigen values and vectors:")
print(np.round(values,2))
print(np.round(vectors,2),"\n")

#checking for orthogonality of the eigenvectors (should be if M is orthogonal)
n1 = 0 # index of vector 1
n2 = 2 # index of vector 2
print(f"The inner product of vector:\n{np.round(vectors.T[n1].reshape((np.shape(vectors.T[n1])[0],1)),2)}\
      \nWith vector:\n{np.round(vectors.T[n2].reshape((np.shape(vectors.T[n2])[0],1)),2)}\n is:\
      \n {inner(vectors.T[n1],vectors.T[n2]):.2f}")
