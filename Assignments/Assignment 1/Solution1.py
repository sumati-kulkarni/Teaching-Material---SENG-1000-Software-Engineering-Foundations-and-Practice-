# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 19:31:40 2020

@author: sumat
"""
import math
#from math import *

print("------------------Question 1------------------")
print(2 * 3)
print(2 ** 3)
print(5+2*5)
print((5 + 2) * 5)
print(-4 - -4 - -4)
print(2 ** 2 ** 0)
print((2 ** 2) ** 0)
print(6 // 2)
print(6 // 4)
print(6.0 / 4.0)
print(2.0 // 2.5)
print(9.0 * 0.5)
print(9.0 ** 0.5)
print(6 % 2)
print(8 % 3)
print(6.2 % 4)
print()

print("------------------Question 2------------------")
print(float(4))
print(int(5.3)  )
print(int(True)  )
print(float(int(5.3))  )
print(int(5.7)  )
print(float(7) // 4)  
print(int(7 / 4)  )
print(6.2 and False)  
print(True and 6.2)  
print(type(4.5)  )
print(type(True and 3))
print()

print("------------------Question 3------------------")
print("\nThe conditional expression with \"and\" will return True only if both operands on it's left and right returns True.", \
      "If the first operand evaluates to be False, the control does not check for the right hand side and simply return False.",\
      "Now, when the operands are 0 and 1, they are treated as False and True respectively for evaluation.",\
      "\n\nFurthermore, if these operands are any number(except 0 and 1) or string, it simply evaluates the whole expression till the last operand encounters, and returns the last value.\n")
print("Example: \n>>> 2 and 3 and 4 and 10 and 2")
print(2 and 3 and 4 and 10 and 7)

print(">>> 1.2 and 5 and \"string\"")
print(1.2 and 5 and "string")

print("\nThe conditional expression with \"or\" will return True if one of the operands returns True.", \
      "If the first operand evaluates to be True, the control does not check for the right hand side and simply return True.",\
      "Again, when the operands are 0 and 1, they are treated as False and True respectively for evaluation.",\
      "\n\nIf these operands are any number(except 0 and 1) or string, returns the first value.\n")
print("Example: \n>>> 2 and 3 and 4 and 10 and 2")
print(2 or 3 or 4 or 10 or 7)

print(">>> 1.2 and 5 and \"string\"")
print(1.2 or 5 or "string")
print()


print("------------------Question 4------------------")
print(min(25, 4)  )
print(max(25, 4)  )
print(min(5,max(7,4))  )
print(abs(25)  )
print(abs(-25)  )
print(round(25.6)  )
print(round(-25.6) ) 
print(round(25.64, 0)  )
print(round(25.64, 1)  )
print(round(25.64, 2)  )
print(len('Hello')  )
print(len('Hello World'))
print(chr(65)  )
print(chr(66)  )
print(ord('A')  )
#print(ord('AB'))
print("ord() takes only one character and gives it's equivalent unicode value. Coz we are passing 'AB', an error is thrown")
print()

print("------------------Question 5------------------")
print(math.sqrt(9)  )
#print(math.sqrt(-9)  )
print("Negative numbers are not in the domain of possible real squares. Instead, the square root of a negative number would need to be complex, which is outside the scope of the Python square root function.")
#print(sqrt(4)  )
print("Calling a function sqrt() directly without using math module")
print(math.floor(3.7)  )
print(math.ceil(3.7)  )
print(math.ceil(-3.7)  )
print(math.trunc(3.7)  )
print(math.trunc(-3.7)  )
print(math.pi  )
print(math.cos(math.pi)  )
print(math.acos(1.0)  )
print(math.e  )
print(math.log(math.e)  )
print(math.log(4,2))
print()

print("------------------Question 6------------------")
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

print("\nAddition: \t\t" , num1 , " + " , num2 , "\t= " , (num1 + num2))
print("Subtraction: \t\t" , num1 , " - " , num2 , "\t= " , (num1 - num2))
print("Multiplication: \t" , num1 , " * " , num2 , "\t= " , (num1 * num2))
print("Division: \t\t" , num1 , " / " , num2 , "\t= " , (num1 / num2))
print("Integer Division: \t" , num1 , " // " , num2 , "\t= " , (num1 // num2))
print("Modulo: \t\t" , num1 , " % " , num2 , "\t= " , (num1 % num2))
print("Exponentiation: \t" , num1 , " ** " , num2 , "\t= " , (num1 ** num2))