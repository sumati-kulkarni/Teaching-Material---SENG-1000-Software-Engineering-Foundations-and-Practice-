class A:
	x = 10
	name = ''
	def __init__(self, nam):
		self.name = nam
		print(self.name,'constructed')
		print('self.x=',self.x)

	def party(self) :
		self.x = self.x + 1
		print(self.name,'party count',self.x)
		print('A.x=',A.x)

s = A('Sally')
j = A('Jim')

s.party()
j.party()
s.party()

