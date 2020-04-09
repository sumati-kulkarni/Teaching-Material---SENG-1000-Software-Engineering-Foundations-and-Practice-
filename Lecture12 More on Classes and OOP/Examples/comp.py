#------------------------------------------------------------
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

	def __str__(self):
		return 'Point ({0}, {1})'.format(self.x, self.y)
   
	def __add__(self,other):
		return Point(self.x + other.x, self.y + other.y)

#------------------------------------------------------------
class Line:
	def __init__(self, p1=None, p2=None):
		self.p1 = p1
		self.p2 = p2
	
	def __str__(self):
		return 'Line: goes from {0} to {1}'.format(self.p1, self.p2)

	# Is this the logic that you need ??!! 	
	def __add__(self,other):
		return Line(self.p1, other.p2)

#------------------------------------------------------------

o1 = Point(1,2)
o2 = Point(2,2)
L1 = Line(o1,o2)
print('o1= ',o1)
print('o2= ',o2)
print('L1= ',L1)

print('.................................')

o3 = Point(10,20)
o4 = Point(20,20)
L2 = Line(o3,o4)
print('o3= ',o3)
print('o4= ',o4)
print('L2= ',L2)

print('.................................')

L3 = L1 + L2 
print('L3= ',L3)
