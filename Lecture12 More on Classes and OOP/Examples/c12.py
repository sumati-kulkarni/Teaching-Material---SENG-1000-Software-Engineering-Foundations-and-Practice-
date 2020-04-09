class A:
	def __init__(self, nam='XXX'):
		self.name = nam
		print(self.name,' is constructed')

	def mA(self):
		print("mA(), name=",self.name)

	def m(self):
		print("m(): from class A, name=",self.name)
		#mA() 		# Error
		self.mA() 	# OKay
		A.mA(self)	# OKay too

a1 = A('a1')
a1.m()

print('[1.......................................]')
		
class B(A):
	def m(self):
		print("m(): from class B, name=",self.name)
		self.mA()			# OKay
		A.mA(self)			# OKay
		A.mA(a1)			# OKay too :)
		super().mA()		# OKay
		super(B,self).mA()	# OKay
		#super(B,a1).mA()	# Error: Not OKay
		super(B,b1).mA()	# OKay

b1 = B('b1')
b1.m()


print('[End.....................................]')