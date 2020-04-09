def f1(var):
	try:
		return int(var)
	except ValueError:
		print('The argument does not contain numbers')

f1("xyz")

def f2( level ):
	try:
		if level < 1:
			raise Exception('InvalidLevel',level)
			# The code below to this would not be executed
			# if we raise the exception
			print('Hummmmmmmmmmmmm.................')
	except Exception as e: #ZeroDivisionError:
		print('WOW!!!!!!!!!!!!!!!!!')
		print(e)
		print(type(e))

try:
	f2(-10)
except Exception:
	print('f2(-10) is bad')
	
	
class MyError(Exception):
	pass
	
def f3( level ):
	if level < 1:
		raise MyError('InvalidLevel',level)
		# The code below to this would not be executed
		# if we raise the exception
		print('Hummmmmmmmmmmmm.................')
try:
	f3(-10)
except MyError:
	print('f2(-10) is bad')