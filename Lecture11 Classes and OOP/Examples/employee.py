class Employee:
   '''Common base class for all employees'''
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print('Total Employee : {0} '.format(Employee.empCount))

   def displayEmployee(self):
      print('Name : {0} Salary : {1}'.format(self.name,self.salary))

'''This would create first object of Employee class'''
emp1 = Employee('First', 2000)
'''This would create second object of Employee class'''
emp2 = Employee('Second', 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee : {0} ".format(Employee.empCount))

print('...............................')
print('Employee.__doc__:', 		Employee.__doc__)
print('Employee.__name__:', 	Employee.__name__)
print('Employee.__module__:', 	Employee.__module__)
print('Employee.__bases__:', 	Employee.__bases__)
import pprint as p
#p.PrettyPrinter(indent=4,width=30)
f = p.pformat(Employee.__dict__)
print(f)