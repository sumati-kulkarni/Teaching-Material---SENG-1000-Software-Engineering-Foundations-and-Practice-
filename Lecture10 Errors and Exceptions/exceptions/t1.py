num =  int(input("Enter a number #1: "))
result = 10/num

try:
    num =  int(input("Enter a number #2: "))
    result = 10/num
    print("Result: ", result)
except ZeroDivisionError:
    print("Exception Handler for ZeroDivisionError")
    print("We cant divide a number by 0")
	
print('.......................')
print('Thanks and Good Bye !!!!')
print('.......................')