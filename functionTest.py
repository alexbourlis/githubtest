class simple:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0

	def setVar(self,x=0,y=0,z=0):
		self.x = x
		self.y = y
		self.z = z


obj=simple()

obj.setVar(1,1,1)

print("x = ",obj.x, " y = ",obj.y, " z = ",obj.z)

def add7(machin:simple):
	return machin.x+7

print(add7(obj))

