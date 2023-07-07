#list comprehensions
square = [i**2 for i in range(10)]

print(square)

even = [element for element in square if element%2 == 0]

print(even)

# lambda is a small anonymous function that can take any amount of arguments but can only have one expression: lambda arguments:expression
# map(fun:iter) fun is a function to which map passes each value of the iterable iter 
numbers = list(map(lambda i: i*10, [i for i in range(1, 6)]))
 
print(numbers)

def f(x):
	return x**2

def g(x):
	return -x

def h(xlist,func):
	try:
		retval = [func(element) for element in xlist]
	except:
		try:
			retval = f(xlist)
		except:
			print("You are giving wrong values")
			retval = None

	return retval

listf = [f,g]
flist = [func(2) for func in listf]
print(flist)
print(h([2,4],f))
#def flist(listoffunc):
