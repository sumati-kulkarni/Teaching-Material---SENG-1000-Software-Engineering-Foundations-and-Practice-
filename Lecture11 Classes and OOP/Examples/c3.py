class A:
	x = 10
	def m1(self):
		print('Hi, I am m1() in A ')
		self.y =20
		self.x =30
		print('A.x=',A.x)
		print('self.y=',self.y)
		print('self.x=',self.x)

print(A.x)
print('.........')
o1 = A()
A.m1(o1)

class B(A):
	x = 2.3
	def m1(self):
		print('Hi, I am m1() in B ')
		self.y =20
		self.x =30
		print('A.x=',A.x)
		print('B.x=',B.x)
		print('self.y=',self.y)
		print('self.x=',self.x)
		B.x +=1
		A.x +=1
		
		print('A.x=',A.x)
		print('B.x=',B.x)
		#self.super.m1() IN Java
		print('.....................')
		super(B,self).m1()
		print('.....................')
		super().m1()
		A.m1(self)

o2 = B()
o2.m1()


print('...................')
print('issubclass(B, A)',issubclass(B, A))
print('issubclass(A, B)',issubclass(A, B))
print('isinstance(o1, A)',isinstance(o2, A))
print('isinstance(o1, B)',isinstance(o1, B))
print('isinstance(o2, B)',isinstance(o2, B))
print('isinstance(o2, A)',isinstance(o2, A))