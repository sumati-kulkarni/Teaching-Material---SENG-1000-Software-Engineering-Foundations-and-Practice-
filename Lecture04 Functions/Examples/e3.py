def fib1(i):
	t1 = 0
	t2 = 1
	if i == 1:
		return t1
	elif i == 2:
		return t2
	else:
		j = 3
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

		
		
def fact1(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * fact1(n-1)

def fact2(n):
	prod = 1
	if n == 0 or n == 1:
		return 1
	else:
		i = 2
		while i <= n:
			prod *= i
			i += 1
		return prod

		
def fact3(n):
	i = n
	prod = i
	i = i - 1
	while i >= 1:
		prod *= i
		i -= 1
	return prod
	
print("fact1(5)=",fact1(5))
print("fact2(5)=",fact2(5))
print("fact3(5)=",fact3(5))
#Testing
x = fib2(1)
y = fib2(2)
z = fib2(8)
print(x,'  ', y,'  ', z)