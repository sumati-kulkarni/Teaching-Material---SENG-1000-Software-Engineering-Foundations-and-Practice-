# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 08:42:31 2020

@author: sumat
"""


filename = input('Enter a filename: ') 
try: 
    infile = open(filename, 'r') 
    contents = infile.read()
    print(contents) 
    infile.close() 
except IOError: 
    print('An error occurred trying to read the file named ', filename) 











# dividebyzero.py
"""Simple exception handling example."""

while True:
    try:
        number = int(input('Enter a number: '))
    except ValueError:
        print('You must enter integer\n')
    else:
        print('You entered number ', number)
        break





while True:
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    except ValueError: 
        print('You must enter two integers\n')
    except ZeroDivisionError: 
        print('Attempted to divide by zero\n')
    else: 
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
        break  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
total = 0.0
try:
    infile = open('sales_data.txt', 'r') 
    for line in infile:
        amount = float(line) 
        total += amount 
        infile.close() 
        print(format(total, ',.2f'))
except: 
    print('An error occured.')
    
    
    
    
    

total = 0.0
try: 
    infile = open('sales_data.txt', 'r') 
    for line in infile: 
        amount = float(line) 
        total += amount 
        infile.close() 
except Exception as err: 
    print(err) 
else: 
    print(format(total, ',.2f'))



def function1():
    function2()
    
def function2():
    raise Exception('An exception occurred')
    
function1()