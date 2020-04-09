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
