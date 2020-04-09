class A:
	y = 0
	def m1() :
		print("Hi, I am m1()")
		#print('y=',y)  # Error
		print('y=',A.y) # OK

A.m1()
A.y =10
A.m1()

class B:
	y = 0
	def m1() :
		print("Hi, I am m1()")
		x =10

B.m1() 
b = B() 
#b.m1()  # Error


class C:
	y = 0
	def m1(self) :
		print("Hi, I am m1()")
		x =10

#C.m1() #Error
c = C()
C.m1(c)
c.m1()  

print('...............................................')
