from B_file1 import ordinal
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def func_one(i,j):
    return (i+j-1)*(i+j)/2 + j + 1

def func_two(i,j):
    return (i+j-1)*(i+j-2)/2 + i        #si l'on remplace le dernier i par j func_two devient func_one ou j est décalé de -1
                                        #donc func_one(i,j)=func_two(i,j+1)

n=4
m=0
if m==0:
    print("f1: the", ordinal(n), "person of the hotel will get the", ordinal(func_one(n, m)), "room")
else:
    print("f1: the", ordinal(n), "person of the", ordinal(m), "bus will get the", ordinal(func_one(n,m)),"room")
copie = m+1
print("f2: the", ordinal(n), "person of the", ordinal(copie), "copie will get the", ordinal(func_two(n,copie)),"room")


fig = plt.figure()
ax = plt.axes(projection='3d')