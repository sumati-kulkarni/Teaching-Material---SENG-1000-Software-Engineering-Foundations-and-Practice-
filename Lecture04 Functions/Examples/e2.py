def fib1(i):
	if i == 1:
		return 0
	elif i == 2:
		return 1
	else:
		j = 3
		t1 = 0
		t2 = 1
		while j <= i:
			t3 = t1 + t2
			t1 = t2
			t2 = t3
			j += 1
		return t3

		
def fib2(i):
	if i == 1:
		return 0
	elif i == 2:
		return 1
	else:
		return fib2(i-1) + fib2(i-2)
		


def fact(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fact(n-1)
		
# Testing
x = fact(1)
y = fact(2)
z = fact(5)
print(x,' ', y, "  ", z)



#x = fib2(1)
#y = fib2(2)
#z = fib2(8)
#print(x,' ', y, "  ", z)