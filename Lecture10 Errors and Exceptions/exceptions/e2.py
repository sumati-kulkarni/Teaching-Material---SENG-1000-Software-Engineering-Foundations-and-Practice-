f = open("test.txt",encoding = 'utf-8')
# perform file operations
f.close()


'''A safer way is to use a try...finally block.'''

try:
	f = open("test.txt",encoding = 'utf-8')
	# perform file operations
finally:
	f.close()
   

'''We don't need to explicitly call the close() method. It is done internally.'''
with open("test.txt",encoding = 'utf-8') as f:
	# perform file operations