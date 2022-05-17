#petit programme test
#from hwcounter import Timer, count, count_end
import numpy as np
import math
import time
#import dis

n = 29000000
nb_loops = 0
tab1 = np.ones(n)
tab0 = np.zeros(n)
tab = np.append(tab1,tab0)
#for i in range(n):
#    tab.append(tab1[i])
#for i in range(n):
#    tab.append(tab0[i])

# Method one
start_time = time.time()
j = 0
while tab[j]:
    j +=1
print("--- %s seconds ---" % (time.time() - start_time))
#print("array size = %d (with method one)" % j)

# Method two
# The array of which we are trying to determine its size is represented by an array of "ones". I created an array of
# "ones" followed by "zeroes". We search the index of the last cell containing a "one" by dichotomy. The goal here is
# to show the huge difference in time efficiency when using a O(log(n)) algorithm instead of a O(n).
start_time = time.time()
if tab[0]==0:
    print("array is empty")
elif tab[1]==0:
    print("array size = 1")
else:
    i = 1
    # We search for a value "outside" of our array
    while tab[i] :
        i = i*2
        nb_loops += 1
    max = i         # index strictly greater than size-1
    min = i/2       # index smaller or equal to size-1
    while(1):
        nb_loops += 1
        if max-min==1:                  # max is always bigger than the index we are searching so M-m=1 means m is the index we are looking for
            size = min +1               # size = last index + 1
            break
        if tab[int((min+max)/2)]:       # checking at the middle of the indexes (min + (max-min)/2)
            min = (min+max)/2
        else:
            max = (min+max)/2
    T = (time.time() - start_time)
    print("--- %s seconds ---" % T)
    #print("array size = %d (with method two)" % size)
    #print("while loop repetitions = %d" % nb_loops)
    print("log base 2 of the size = %d" % int(math.ceil(math.log(size, 2))))

#dis.dis(dis)
