# input() function allows the user to take input from the keyboard as a string. 
# It is important to note that the output of input is always a string (even is a number is entered).

a = input("Enter number 1: ")
b = input("Enter number 2: ")
print("Sum is ", a + b)

# In order to acheieve that we want i.e sum of 2 numbers on users input
# We need to type-cast the input string type to number i.e, int

c = int(input("Enter number 1: "))
d = int(input("Enter number 2: "))
print("Sum is ", c + d)
