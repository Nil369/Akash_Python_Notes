# Write a python function to print multiplication table of a given number. 

def multiply(n):
    for i in range(1, 13):
        print(f"{n} X {i} = {n*i}")

input = int(input("Enter a number you want table of: "))
multiply(input)