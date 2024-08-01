# write a program to swap two numbers without using third Variables.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
print(f"Before swapping: a = {a}, b = {b}")
a = a + b 
b = a - b 
a = a - b 
print(f"After swapping: a = {a}, b = {b}")

