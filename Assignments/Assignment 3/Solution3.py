# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 12:30:42 2020

@author: Sumati Kulkarni
"""


print("\n---------------------------Question 1---------------------------")
sentence = "The quick brown fox jumped over the lazy dog. The preceding sentence has the special property that it has all the twenty-six English alphabetic characters appearing in it. Could you come up with another sentence which has the same property?"
sentence = sentence.strip(".,?/");
for str in sentence.lower().split():
    if(str.startswith("a") or str.startswith("e") or str.startswith("i") or str.startswith("o") or str.startswith("u")):
        print(str)

print("\n---------------------------Question 2---------------------------")      
string = input("Please enter a string : ")
string = string.lower()
if(string == string[:: - 1]):
   print("This is a Palindrome")
else:
   print("This is Not a Palindrome")
   
print("\n---------------------------Question 3---------------------------")     
print("Please enter the following \n")
firstName = input("Firstname : ")
lastName = input("Lastname : ")
year = input("Year Of Joining : ")

print("\nHi "+ firstName.capitalize()+ ",\n\nWelcome to ECU.")
print("\nYour email-id is: "+ lastName.lower() + firstName.lower()[:1] + year[-2:] + "@students.ecu.edu.\n\nThank you.")

print("\n---------------------------Question 4---------------------------")     
import math
n = int(input("Enter value of N: "))

print("Enter ", n, " values")

nums = []
sum = 0.0
for i in range(0, n):
    nums.append(float(input()))
    sum = sum + nums[i]
    
mean = sum/n

print("SUM: ", sum)
print("MEAN: ", mean)

squared = 0.0
for i in range(0, n):
    squared += (nums[i] - mean)**2
print("SD: ", math.sqrt(squared/n)) 

print("\n---------------------------Question 5---------------------------")
def sortRecords(records):  
    n = len(records)  
    for i in range(0, n):  
          
        for j in range(0, n-i-1):  
            if (records[j][0] > records[j + 1][0]):  
                temp = records[j]  
                records[j]= records[j + 1]  
                records[j + 1]= temp  
    return records

def insertRecord():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height: "))
    record = (name, age, height)
    return record

def printRecords(records):
    print("\n----Records----\n")
    for record in records:
        print(record)

def deleteRecord(name, records):
    result = [] 
    flag = False
    for item in records: 
        if item[0] != name: 
            result.append(item)
        else:
            flag = True
    if(flag):
        print("Record "+ name + " deleted successfully\n")
    return result
    
records = []
while (True): 
    print("\n1 -> Insert a record") 
    print("2 -> Delete a record") 
    print("3 -> Sort the list") 
    print("4 -> Display list") 
    print("5 -> Exit") 
    ch = int(input("Enter your choice: "))
    
    if(ch == 1):
        records.append(insertRecord())
    elif(ch == 2):
        name1 = input("Enter name of the record you want to delete : ")
        records = deleteRecord(name1, records)
    elif(ch == 3):
        records = sortRecords(records)
        print("Records sorted Successfully\nDisplay to view sorted list")
    elif(ch == 4):
        printRecords(records)
    elif(ch == 5):
        break
        
    
print("\n---------------------------Question 6---------------------------")
dictionary = {"E0001" : {"name" : "Aaron", "education" : "BS in CS", "year_of_joining" : 2001, "salary" : 1234.5},
              "E0002" : {"name" : "Bill", "education" : "BS in Mechanical", "year_of_joining" : 2004, "salary" : 5000.123},
              "E0003" : {"name" : "Clark", "education" : "MS in CS", "year_of_joining" : 2007, "salary" : 4002.6},
              "E0004" : {"name" : "Den", "education" : "BS in Electrical", "year_of_joining" : 2001, "salary" : 2000.8},
              "E0005" : {"name" : "Emily", "education" : "MS in Mechanical", "year_of_joining" : 2002, "salary" : 8000.12}
              }

for key, value in dictionary.items():
    value["salary"] += (0.01) * value["salary"]
    value["company"] = "Apple"
    print(key, ", ", value["name"], ", ", value["education"], ", ", value["year_of_joining"], ", ", value["salary"], ", ", value["company"])

dictionary.pop("E0004")    
print("\n---------------------------Question 7---------------------------")         

engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])

employees = engineers | programmers | managers

print(employees)

engineering_management = engineers & managers

print(engineering_management)

fulltime_management = managers - engineers - programmers

print(fulltime_management)

engineers.add("Marvin")

if(employees.issuperset(engineers)):
    print("Employees is super set of Engineers")
    
employees.update(engineers)

if(employees.issuperset(engineers)):
    print("Employees is super set of Engineers")
    
for group in [engineers, programmers, managers, employees]:
    group.discard("Susan")