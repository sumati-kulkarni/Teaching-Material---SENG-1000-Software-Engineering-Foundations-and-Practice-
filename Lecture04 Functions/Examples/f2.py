print("0.................")
def f1(k):
	i = 0
	while i <= k:
		print('i=',i)
		i += 1

		
f1(10)	
	
print("1.................")

def f2(k):
	if k < 0:	
		return
	f2(k-1)
	print('k=',k)

f2(10)	
	
print("2.................")

print("3.................")

def f3(k):
	i = k
	while i >= 0:
		print('i=',i)
		i -= 1

f3(10)	
	
print("4.................")

def f4(k):
	if k < 0:	
		return
	print('k=',k)
	f4(k-1)

f4(10)	
	
print("5.................")