class A:
	def __init__(self, nam='XXX'):
		self.name = nam
		print(self.name,' is constructed')

	def mA(self):
		print("mA(), name=",self.name)

	def m(self):
		print("m(): from class A, name=",self.name)

a1 = A('a1')
a1.m()

print('[1.......................................]')
		
class B(A):
	def m(self):
		print("m(): from class B, name=",self.name)

b1 = B('b1')
b1.m()

print('[2.......................................]')

print('issubclass(B, A)',issubclass(B, A))
print('issubclass(A, B)',issubclass(A, B))
print('isinstance(a1, A)',isinstance(a1, A))
print('isinstance(a1, B)',isinstance(a1, B))
print('isinstance(b1, A)',isinstance(b1, A))
print('isinstance(b1, B)',isinstance(b1, B))

print('[End.....................................]')