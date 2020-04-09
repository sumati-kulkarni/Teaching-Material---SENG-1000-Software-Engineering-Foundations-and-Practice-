from pprint import pprint

class A:
	x = 0
	name = ''
	def __init__(self, nam):
		self.name = nam
		print(self.name,' is constructed')

	def m1(self):
		self.x = self.x + 1
		print("name=",self.name,"\nx=:",self.x)

class B(A):
	points = 0

	def m2(self):
		self.points = self.points + 1
		self.m1()
		print("name=",self.name,"\npoints:",self.points)

o1 = A("o1 object")
o1.m1()
#pprint(dir(o1))

print('-------------------')

o2 = B("o2 object")
o2.m1()
o2.m2()
#pprint(dir(o2))