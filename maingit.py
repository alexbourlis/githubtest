#petit programme test
#from hwcounter import Timer, count, count_end
import numpy as np
import math
import time
#import dis

n = 3000000
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
start_time = time.time()
if tab[0]==0:
    print("array is empty")
elif tab[1]==0:
    print("array size = 1")
else:
    i = 1
    while tab[i] :
        i = i*2
        nb_loops += 1
    max = i
    min = i/2
    while(1):
        nb_loops += 1
        if max-min==1:
            size = min +1
            break
        if tab[int((min+max)/2)]:
            min = (min+max)/2
        else:
            max = (min+max)/2
    T = (time.time() - start_time)
    print("--- %s seconds ---" % T)
    #print("array size = %d (with method two)" % size)
    #print("while loop repetitions = %d" % nb_loops)
    print("log base 2 of the size = %d" % int(math.ceil(math.log(size, 2))))

#dis.dis(dis)
