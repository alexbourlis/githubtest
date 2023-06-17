import numpy as np
from numpy.linalg import norm
import matplotlib.pyplot as plt
import time

time_one = time.perf_counter()

shape = (11,11)
grid = np.zeros(shape)
point = [5,5]
grid[*point]=10


size =3
lower_bound_x,upper_bound_x = point[0]-size,point[0]+size+1
lower_bound_y,upper_bound_y = point[1]-size,point[1]+size+1
zone = grid[lower_bound_x:upper_bound_x,lower_bound_y:upper_bound_y]
x,y = np.where(zone == 0)
surrounding_points = np.vstack((x,y)).T+point-size


distance = norm(surrounding_points-point,axis= 1)
for count,dist in enumerate([10**0.5,5**0.5,2**0.5]):
	indexes = np.where(distance <= dist)
	grid[surrounding_points[indexes].T[0],surrounding_points[indexes].T[1]] = count+1

print("time elapsed: ",time.perf_counter()-time_one)


plt.imshow(grid)
plt.show()
