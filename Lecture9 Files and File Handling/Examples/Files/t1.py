print('.................................................')
#To open a text file, use
f = open('t1.txt', 'r')
s = f.read()
print(s)
if f.closed:
	print("File Closed already !!!!")
else:
	f.close()
	print("Now the File is Closed !!!!")

print('.................................................')	
print('1[#To read a text file, use:]....................')
print('.................................................')

#To read a text file, use:
f = open("t1.txt","r")
print(f.read())

print('.................................................')
print('2[#To read one line at a time, use:].............')
print('.................................................')

#To read one line at a time, use:
f = open("t1.txt", "r")
print(f.readline())

print('.................................................')
print('3[#To read a list of lines use:].................')
print('.................................................')

#To read a list of lines use:
f = open("t1.txt", "r")
print(f.readlines())

print('.................................................')
print('4[#To write to a file, use:].....................')
print('.................................................')

#To write to a file, use:
f = open("hello.txt","w")
f.write("Hello World!!!!")
f.close()

print('.................................................')
print('5[#To write to a file, use:].....................')
print('.................................................')

#To write to a file, use:
f = open("hello.txt", "w")
lines_of_text = ["a line of text", "another line of text", "a third line"]
f.writelines(lines_of_text)
f.close()
print('.................................................')
print('6[#To append to file, use:]......................')
print('.................................................')

#To append to file, use:
f = open("Hello.txt", "a")
f.write("Hello World again")
f.close

print('.................................................')
print('7[#To close a file, use].........................')
print('.................................................')

#To close a file, use
f = open("hello.txt", "r")
print(f.read())
f.close()
print('.................................................')
