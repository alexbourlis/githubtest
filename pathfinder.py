import numpy as np
import time
import random as rd
from math import floor
from matplotlib import pyplot as plt

rd.seed(13)#13

start_time = time.perf_counter()

#-------- 20x20 map with random obstacles (1==obstacle)-----#
list1 = np.zeros((20,20))
for i in range(10):
    x,y = floor(rd.uniform(0,20)),floor(rd.uniform(0,20))
    list1[x,y] = -1
list1[13,15]=-1
list1[13,14]=-1
list1[12,14]=-1
list1[12,13]=-1
list1[15,10]=-1


#-----------------------------------------------------------#

# list of the indexes for points with value 1 (list of obstacles indexes)
u = np.where(list1==-1)
v = np.vstack((u[0],u[1])).T    

# labeling the non-allowed blocks with 7
r = 1 #radius of non allowed blocks
for i,p in enumerate(v):
    mask = list1[max(p[0]-r,0):p[0]+r+1,max(p[1]-r,0):p[1]+r+1] !=-1
    list1[max(p[0]-r,0):p[0]+r+1,max(p[1]-r,0):p[1]+r+1] = mask*7\
     + (~mask)*list1[max(p[0]-r,0):p[0]+r+1,max(p[1]-r,0):p[1]+r+1]

#starting position
start = [3,3]
list1[start[0],start[1]] = 9
#goal
goal = [17,18]
list1[goal[0],goal[1]] = 5
#Radius of research and length of zone of reasearch
R = 1
L = 50 
#list of the path points in order
chain = []
 
#moving the goal if needed
rg = 1
while (list1[max(goal[0]-rg,0):goal[0]+rg+1,max(goal[1]-rg,0):goal[1]+rg+1] == -1).sum() != 0:
    list1[goal[0],goal[1]] = 0
    goal[0]=goal[0]-1
    list1[goal[0],goal[1]] = 5

#creating the path
goal_reached = False
class Goal_reached(Exception): pass
try:
    while goal_reached==False:
        reference = start
        i = 0
        while i < L:
            # mask:(2R+1)x(2R+1) surrounding array with the allowed places
            lower_bound_x,upper_bound_x= max(reference[0]-R,0),reference[0]+R+1
            lower_bound_y,upper_bound_y= max(reference[1]-R,0),reference[1]+R+1
            mask = list1[lower_bound_x:upper_bound_x,lower_bound_y:upper_bound_y] == 0 #or 1
            # if we find a square with value 5 it means we have found the goal
            if (list1[lower_bound_x:upper_bound_x,lower_bound_y:upper_bound_y] == 5).sum() != 0:
                #if reference == start:
                if ((start[0]-np.array(goal)[0])**2+(start[1]-np.array(goal)[1])**2)**0.5 <= 18**0.5: 
                    raise Goal_reached
                break
        
            #surrounding_points contains the list of coordinates of allowed places, if statement to verify for dead ends
            a = np.where(mask==True)[0]
            b = np.where(mask==True)[1]
            surrounding_points = np.vstack((a,b)).T + reference-R
            if len(surrounding_points) != 0:
                surrounding_points -= [min(0,surrounding_points.T.min()), min(0,surrounding_points.T.min())] #readjusting the scale
                distance = ((goal[0]-surrounding_points.T[0])**2+(goal[1]-surrounding_points.T[1])**2)**0.5
                index_min = np.where(distance==distance.min())[0][0]
                reference = surrounding_points[index_min].tolist()
                chain.append(reference)
                list1[reference[0],reference[1]] = 2
            else:
                if len(chain) != 0:
                    chain.pop(-1)
                    list1[reference[0],reference[1]] = 7 # 7 stands for non allowed block
                    reference = chain[-1]
                else:
                    print("to be handled") #when chain is empty, which means we are close to the goal, handled before
        
            
            i = (abs(np.array(start)-np.array(reference))).max()
            plt.imshow(list1,cmap='plasma')
            plt.pause(0.1)
        
        distance = ((start[0]-np.array(chain).T[0])**2+(start[1]-np.array(chain).T[1])**2)**0.5
        indexes_close = np.where(distance<=8**0.5)[0]
        list1[np.array(chain)[indexes_close].T[0],np.array(chain)[indexes_close].T[1]] = 0
        for i in reversed(indexes_close):
            chain.pop(i)

        plt.imshow(list1,cmap='plasma')
        plt.pause(0.5)
    
        list1[start[0],start[1]] = 0

        start = chain[0]
        list1[np.array(chain).T[0],np.array(chain).T[1]]=0
        list1[start[0],start[1]] = 9
        chain = []
except Goal_reached:
    print("Goal_reached")

print("time elapsed: ", time.perf_counter()-start_time)

plt.imshow(list1)#,cmap='gray')

plt.show()




