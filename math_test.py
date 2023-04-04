# testing math functions
import math

sum = 0
n = 100000

for i in range(n):
    sum += math.sqrt(1+i/n/n)-1

#print("the sum is equal to: %f" % sum)

nb_roots = 5
roots1 = []
roots2 = []
for k in range (nb_roots):
    roots1.append(k/3-1/12)
    roots2.append(k/3 + 1/4)

print(roots1)
print(roots2)
print(roots2[4]-roots1[0])
print(math.sin(math.pi*roots2[4]))
print(math.sin(math.pi*roots1[0]))