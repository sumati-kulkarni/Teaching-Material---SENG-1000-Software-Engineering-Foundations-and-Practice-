def main():
    call_me(31, 93, 62)
    call_me(93, 62, 31)
    print("\n")
    call_me(a=31, b=93, c=62)
    call_me(c=62, b=93, a=31)
    print("\n")
    
    print(different_call_me(1, 2))		# returns 3, positional and default. 
    print(different_call_me (1, 2, 3)) 		# returns 5, positional. 
    print(different_call_me(c = 5, b = 2, a = 2)) 	# returns 9, named. 
    print(different_call_me(b = 2, a = 2))		# returns 5, named and default. 
    print(different_call_me(5, c = 2, b = 1)) 	# returns 7, positional and named. 
    print(different_call_me(8, b = 0)) 		# returns 1, positional, named and default.
    
    
def call_me(a, b, c):
    print("a = ", a, " b = ", b, " c = ", c )
    
def different_call_me(a, b, c = 1): # a/b required, c optional. 
    return a * b + c
    
if __name__== "__main__":
    main()