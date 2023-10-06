# Expanding numpy
# https://numpy.org/doc/stable/user/basics.subclassing.html#implications-for-subclassing
import numpy as np
class RealisticInfoArray(np.ndarray):

    def __new__(cls, input_array, info=None):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # add the new attribute to the created instance
        obj.info = info
        #Complex Transpose a.k.a. adjoint
        obj.CT = np.conjugate(obj.T)
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        if obj is None: return
        self.info = getattr(obj, 'info', None)
        self.CT = getattr(obj,'CT', None)

arr = np.array([1,2])*1j
print(arr)
obj = RealisticInfoArray(arr, info='information')
print(obj.CT)
print(type(obj))
print(obj.info)
v = obj[1:]
print(type(v))
print(v.CT)