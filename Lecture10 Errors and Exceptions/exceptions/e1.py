#x = 10
#y = 0
#print(x/y)

#x = float(input('x='))
#y = float(input('y=')) # Error if y==0
#print('x/y',x/y)

try:
	x = float(input('x='))
	y = float(input('y='))
	print('x/y',x/y)
except : #ZeroDivisionError as e:#ZeroDivisionError:#ValueError:
	print('Something went wrong !!!')
	#print('e=',e)
	#print('type(e)=',type(e))
finally:
	print('finally block will be always executed regardless of the error')
print('Good Bye!!!')