# WRITE A PROGRAM in Python to find the maximum between three numbers.

# Sol 1 using if-else:

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

if(a>b and a>c):
    print(f"The largest number is: {a}")
elif(b>a and b>c):
    print(f"The largest number is: {b}")
elif(c>a and c>b):
    print(f"The largest number is: {c}")



# Sol 2 using List:

"""
l = []
for i in range(1,4):
    n = int(input(f"Enter number {i} : "))
    l.append(n)

maxi = max(l)
print(maxi)

"""