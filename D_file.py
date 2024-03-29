from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def ordinal(number):
    if number==0: return "ERROR"
    elif number==1: return "1st"
    elif number==2: return "2nd"
    elif number==3: return "3rd"
    else: return "%dth" % number
    
def func_one(i,j):
    return (i+j-1)*(i+j)/2 + j + 1

def func_two(i,j):
    return (i+j-1)*(i+j-2)/2 + i        #si l'on remplace le dernier i par j func_two devient func_one ou j est décalé de -1
                                        #donc func_one(i,j)=func_two(i,j+1)

n=1
m=1
if m==0:
    print("f1: the", ordinal(n), "person of the hotel will get the", ordinal(func_one(n, m)), "room")
else:
    print("f1: the", ordinal(n), "person of the", ordinal(m), "bus will get the", ordinal(func_one(n,m)),"room")
copie = m+1
print("f2: the", ordinal(n), "person of the", ordinal(copie), "copie will get the", ordinal(func_two(n,copie)),"room")


fig = plt.figure()
ax = plt.axes(projection='3d')