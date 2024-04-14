# OOPs = Object Oriented Programming
class Employee:
    def __init__(self, name, salary): #CONSTRUCTER
        self.name = name
        self.salary = salary

    def getSalary(self):
        print(self.salary())

rohan = Employee("Rohan", "34500")
print(rohan.salary)
print(rohan.name)

Akash = Employee("Akash", "999999000000000")
print(Akash.salary)
print(Akash.name)
