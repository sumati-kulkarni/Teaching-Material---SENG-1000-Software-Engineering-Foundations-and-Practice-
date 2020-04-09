def fib1(i):
	if i == 1:
		return 0
	elif i == 2:
		return 1
	else:
		s1 = 0
		s2 = 1
		j = 3
		while j <= i:
			s3 = s1 + s2
			s1 = s2
			s2 = s3
			j += 1
		return s3

def fib2(i):
	if i == 1:
		return 0
	elif i == 2:
		return 1
	else:
		return fib2(i-1) + fib2(i-2)
		
def fact2(i):
	if i == 0 or i == 1:
		return 1
	else:
		return i * fact2(i - 1)

x = fact2(0)
y = fact2(3)
z = fact2(5)
print(x," ",y,' ',z)
		
#x = fib2(1)
#y = fib2(2)
#z = fib2(7)
#print(x," ",y,' ',z)




	
def outNums(i,j):
  i = int(i)
  j = int(j)
  while i <= j:
    print(i)
    i = i + 1
	
#print("hiiiiiiiiiii")

def read():
  x = input('x=')
  y = input('y=')
  outNums(x,y)

#outNums(10,20)
#read()
  
def main():
    value = 99
    print("Value ", value)
    change_me(value)
    print(value)
    
def change_me(value):
    value = 0
    
#if __name__== "__main__":
#    main()