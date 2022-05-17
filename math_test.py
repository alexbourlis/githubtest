# testing math functions
import math

sum = 0
n = 100000

for i in range(n):
    sum += math.sqrt(1+i/n/n)-1

print("the sum is equal to: %f" % sum)