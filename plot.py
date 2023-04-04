import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

def plot_shit():
    # ..................setting the plot..................#
    # plt.plot(x, y, 'o')
    # plt.bar(0,20,width=0.11,bottom=-10)
    # plt.barh(0,20,height=0.11,left=-10,color='blue')
    plt.arrow(0, 0, x, y, length_includes_head=True, head_width=0.3)
    plt.vlines(0, -20, 20)
    plt.hlines(0, -10, 10)
    # plt.axhline()
    # plt.legend('points')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.ylabel('x')
    plt.xlabel('y')
    plt.title('2d cartesian')
    plt.grid(True)
    # plt.tight_layout()
    plt.show(block=False)
    # ...................plot set.........................#
#plt.style.use('bmh')
def left(x0,y0):
    x = -y0
    y = x0
    return x,y

def right(x0,y0):
    x = y0
    y = -x0
    return x,y

x = 1
y = 9

plot_shit()

i = 1
print('hello')
while i>0:
    print('type right or left or stop')
    dir = input()
    if dir == 'right':
        x,y = right(x,y)
    elif dir == 'left':
        x,y = left(x,y)
    elif dir == 'stop':
        break
    else:
        print('invalid entry')
    plt.arrow(0,0,x,y,length_includes_head=True,head_width=0.3)

plt.show()