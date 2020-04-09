
class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector ({0}, {1})'.format(self.a, self.b)
   
	def __add__(self,other):
		return Vector(self.a + other.a, self.b + other.b)
	
	def __iadd__(self,other):
		return Vector(self.a + other.a, self.b + other.b)
	
	def __sub__(self,other):
		return Vector(self.a - other.a, self.b - other.b)

	def __mul__(self,other):
		return Vector(self.a * other.a, self.b * other.b)

	def	__truediv__(self,other):
		return Vector(self.a / other.a, self.b / other.b)

	def	__floordiv__(self,other):
		return Vector(self.a // other.a, self.b // other.b)

		

v1 = Vector(2,10)
v2 = Vector(5,3)
print('v1 + v2',v1 + v2)
print('v1 - v2',v1 - v2)
print('v1 * v2',v1 * v2)
print('v1 / v2',v1/v2)
print('v1 // v2',v1//v2)

v3 = Vector(1,1)
v3 += v2
print(v3)