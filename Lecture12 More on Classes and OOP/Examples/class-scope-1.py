class A:
	a1 = 10
	def __init__(self, x=1, y=2):
		self.a = x
		self.b = y
		print('A Constructor !!!')
	def __del__(self):
		print('A Destructor !!!')
	
	def m1():
		print('m1() from the A class')
		
	def m2(self):
		print('m2() from the A class')
	
	def m3(self):
		print('-----------------starting m3() from the A class')
		print('self.a  =', self.a)
		print('self.b  =', self.b)
		print('self.a1 =', self.a1)
		print('A.a1    =', A.a1)
		print('-----------------ending m3() from the A class')

print('[00]...................')
A.m1() 		# OKay
#A.m2() 	# NOT OKay
A.m2(-999) 	# Now it is OKay
#A.m3(-999) # NOT OKay

print('[01]...................')
o1 = A()
print('[03]...................')
A.m3(o1)	# 100% Okay
print('[04]...................')
o1.m3()		# 100% Okay
print('[05]...................')
print(A.a1)
A.a1 = 9999
print(A.a1)
print('[06]...................')
o1.m3()		# 100% Okay
print('[07]...................')
print(A.a1) # !!!!
o1.a1 = 77777
o1.m3()		# 100% Okay
print(A.a1) # ????
print('[08]...................')
o1.h = '???????'
A.k = '!!!!!!'
print('o1.h=',o1.h)
print('A.k=',A.k)
print('o1.k=',o1.k)
print('[09]...................')
