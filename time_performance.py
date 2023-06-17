import numpy as np
import time
from numba import jit



@jit(nopython=True)
def ones_arr(n):
	arr = []
	for i in range(n):
		internal_arr = []
		for j in range(n):
			internal_arr.append(1)
		arr.append(internal_arr)
	return arr

n = 1000
#method 1
start_time = time.perf_counter()

arr = np.full((n,n),3)
arr2 = np.eye(n)
arr3 = arr2.dot(arr)

print("time: {:.10f} s " .format(time.perf_counter()-start_time))

##method 3
#start_time = time.perf_counter()
#arr = ones_arr(n)
#print("time: {:.10f} s " .format(time.perf_counter()-start_time))
#
##method 2
#start_time = time.perf_counter()
#arr = []
#for i in range(n):
#	internal_arr = []
#	for j in range(n):
#		internal_arr.append(1)
#	arr.append(internal_arr)
#print("time: {:.10f} s " .format(time.perf_counter()-start_time))

		
