# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 15:39:00 2020

@author: sumati kulkarni
"""

def describeNumber(number):
    if(number > 0):
        if(number%2 == 0):
            return str(number) + " is positive even number"
        else:
            return str(number) + " is positive odd number"
    elif(number < 0):
        if(number%2 == 0):
            return str(number) + " is negative even number"
        else:
            return str(number) + " is negative odd number"
    else:
        return str(number) + " is either positive or negative"

def isLeapYear(year):
    return (((year % 4) == 0) or ((year % 400) == 0) & ((year % 100) != 0))

def isPrime(number):
    if number >= 2:
        for n in range(2, number):
            if not ( number % n ):
                return False
    else:
        return False
    return True

def printMultiplicationTable(m):
    for i in range(1, 11):
        print(m, " x ", i, " = ", (m*i))

def displayAnswer5():
    pass
    
def displaySquaresRange(start, end):
    for i in range(start, end+1):
        print(i, " -> ", (i*i))
  
def convertFahrenheitToCelcius(num):
    return  ((num - 32) * (5.0/9.0))

def addComplex(r1, i1, r2, i2):
    print("\nAddition : (", r1, "+", i1, "i) + (", r2, "+", i2, "i) = (", (r1 + r2), "+", (i1+i2), "i)")
  
def getReversedNumber(num):
    reverse = 0    
    while(num > 0):    
        i = num %10    
        reverse = (reverse *10) + i    
        num = num //10
    return reverse
    
def main():
    print("------------------Question 1------------------")
    num = int(input("Enter a number : "))
    print(describeNumber(num));
    
    print("\n------------------Question 2------------------")
    year=int(input("Enter year : "))
    if(isLeapYear(year)):
        print(year,"is a leap year".format(year))
    else:
        print(year,"is not a leap year".format(year))
        
    print("\n------------------Question 3------------------")
    num = int(input("Enter a number : "))
    if(isPrime(num)):
        print(num, " is Prime")
    else:
        print(num, " is not Prime")
        
    print("\n------------------Question 4------------------")
    num = int(input("Enter a number : "))
    print("\nMultiplication Table\n")
    printMultiplicationTable(num)
    
    print("\n------------------Question 5------------------")
    displayAnswer5()
    
    print("\n------------------Question 6------------------")
    start = int(input("Starting Range : "))
    end = int(input("Ending Range : "))
    
    if(start < end):
        print("Squares")
        displaySquaresRange(start, end)
    else:
        print("Invalid Range")
    
    print("\n------------------Question 7------------------")
    
    print("\n------------------Question 8------------------")
    num = float(input("Enter a Fahrenheit value: "))
    print("Celcius : ", convertFahrenheitToCelcius(num))
    
    print("\n------------------Question 9------------------")
    print("Enter First Complex Number : ")
    r1 = float(input("Real Part : "))
    i1 = float(input("Imaginary Part : "))
    
    print("\nEnter Second Complex Number : ")
    r2 = float(input("Real Part : "))
    i2 = float(input("Imaginary Part : "))
    
    addComplex(r1, i1, r2, i2)
        
    print("\n------------------Question 10------------------")
    num = int(input("Enter a number : "))  
    print("Reversed Number : ", getReversedNumber(num))
    
if __name__== "__main__":
  main()

