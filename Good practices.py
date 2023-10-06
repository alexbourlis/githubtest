# Good practices
t = 1.1234567890
print(f"my value is {t:.2f}\n")

# indexing techniques with 2d arrays
import numpy as np
x = np.eye(4)
x[0,2] = 2
print("Original grid:\n",x)
mask = (x==1) + (x==2)
print("filtered values:\n",mask)
list = np.argwhere(mask)
print("list of points with desired property:\n",list)
#changing their value
x[list.T[0],list.T[1]] = np.array([1,2,3,4,5])
print("final result:\n",x)
print(x[mask])