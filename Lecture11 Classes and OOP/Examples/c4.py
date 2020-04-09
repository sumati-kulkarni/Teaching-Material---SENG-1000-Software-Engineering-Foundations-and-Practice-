class A:
	y = 0
	def m1() :
		print("Hi, I am m1()")
		#print('y=',y)  # Error
		print('y=',A.y) # OK

A.m1()
A.y =10
A.m1()

class B:
	y = 0
	def m1() :
		print("Hi, I am m1()")
		x =10

B.m1() 
b = B() 
#b.m1()  # Error


class C:
	y = 0
	def m1(self) :
		print("Hi, I am m1()")
		x =10

#C.m1() #Error
c = C()
C.m1(c)
c.m1()  

print('...............................................')

from pprint import pprint

def myPrint(o):
	print('---------------------')
	print ("Type", type(o))
	print ("Dir ")
	pprint(dir(o))
	print ("Type", type(o.x))
	print ("Type", type(o.m1))
	print('---------------------')

class A:
	y = 0

	def __init__(self):
		self.x = 0
		#y = 0
		print('I am constructed')

	def __del__(self):
		print('I am destructed', self.x)

	def m1(self) :
		self.x = self.x + 1
		self.y = self.y + 1 
		print("So far x=",self.x," and y =" ,self.y)

o1 = A()
o1.m1()
o1.m1()
o1.m1()
A.m1(o1)
print(A.y)
A.y += 1

#myPrint(o1)

o2 = A()
o2.m1()
o2.m1()
o2.m1()
A.m1(o2)
print(A.y)

#myPrint(o2)

o1 = 10
print("o1=",o1)

print('...............................................')

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
