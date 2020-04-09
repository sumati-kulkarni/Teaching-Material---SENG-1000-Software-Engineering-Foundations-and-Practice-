# define Python user-defined exceptions
class MyError(Exception):
	'''Base class for other exceptions'''
	pass

class ValueTooSmallError(MyError):
	'''Raised when the input value is too small'''
	pass

class ValueTooLargeError(MyError):
	'''Raised when the input value is too large'''
	pass

# our main program
# user guesses a number until s/he gets it right

# you need to guess this number
number = 10

while True:
	try:
		i_num = int(input("Enter a number: "))
		if i_num < number:
			raise ValueTooSmallError
		elif i_num > number:
			raise ValueTooLargeError
		break
	except ValueTooSmallError:
		print("This value is too small, try again!\n\n")
	except ValueTooLargeError:
		print("This value is too large, try again!\n\n")

print("Congratulations! You guessed it correctly.")