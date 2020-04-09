class A:
	a1 = 10
	def __init__(self, x=1, y=2):
		self.a = x
		self.b = y
		self.__z = x + y
		print('A Constructor !!!')
	
	def __del__(self):
		print('A Destructor !!!')
	
	def m(self):
		print('--starting m() from the A class')
		print('self.a  	=', self.a)
		print('self.b  	=', self.b)
		print('self.__z =', self.__z)
		print('self.a1 	=', self.a1)
		print('A.a1    	=', A.a1)
		print('--ending m() from the A class')

print('[00]......................................')
o1 = A()
print()

print('[01]......................................')
A.m(o1)		# 100% Okay
print()

print('[03]......................................')
o1.m()		# 100% Okay
print()

print('[04]......................................')
print(A.a1)
A.a1 = 9999
print(A.a1)
print()

print('[05]......................................')
o1.m()		# 100% Okay
print()

print('[06]......................................')
print(A.a1) # !!!!
o1.a1 = 77777
o1.m()		# 100% Okay
print(A.a1) # ????
print()

print('[07]......................................')
