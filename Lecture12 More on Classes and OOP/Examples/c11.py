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
B.m(b1)
B.m(a1) 		# Interestingly works just fine :)
super(B,b1).m() # almost B.A.m(b1), this does not work


print('[End.....................................]')