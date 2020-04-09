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
		self.__init__()
		self.__del__()

o1 = A()
o1.m1()
#A.m1(o1)

