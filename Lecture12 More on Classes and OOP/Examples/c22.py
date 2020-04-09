class A:
	def __init__(self, nam='XXX'):
		self.name = nam
		print(self.name,' is constructed')

	def mA(self):
		print("mA(), name=",self.name)

a1 = A('a1')
a1.mA()

print('[1.......................................]')
		
class B(A):
	def mB(self):
		print("mB(), name=",self.name)


b1 = B('b1')
b1.mB()

print('[2.......................................]')

class C(A):
	def __init__(self,name):
		self.x = 10
		self.y = 20
		A.__init__(self, name)  		# OKay
		super(C,self).__init__(name)	# and this is Okay too
		super().__init__(name)			# Okay too, single inheritance
	def mC(self):
		print("mC(), name=",self.name)
		print('(',self.x,',',self.y,')')


c1 = C('c1')
c1.mC()
c1.mA()


print('[End.....................................]')